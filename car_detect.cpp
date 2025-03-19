#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

// Klasa przechowująca informacje o detekcji
struct Detection {
    cv::Rect box;
    float confidence;
    int classId;
};

class CarCounter {
public:
    // Konstruktor ładuje sieć z pliku ONNX (np. "yolov8n.onnx")
    explicit CarCounter(const std::string& modelPath)
    {
        // Wczytanie modelu YOLO w formacie ONNX
        net_ = cv::dnn::readNetFromONNX(modelPath);
        if (net_.empty()) {
            throw std::runtime_error("Nie udało się wczytać modelu z: " + modelPath);
        }

        // (Opcjonalne) Ustawienie preferencji wykonywania (CPU/GPU):
        // net_.setPreferableBackend(cv::dnn::DNN_BACKEND_OPENCV);
        // net_.setPreferableTarget(cv::dnn::DNN_TARGET_CPU);

        std::cout << "Model załadowany: " << modelPath << std::endl;
    }

    // Metoda analogiczna do get_car_detections z Pythona
    // Zwraca listę wykryć o klasie = 2 (car)
    std::vector<Detection> getCarDetections(const std::string& imagePath)
    {
        cv::Mat image = cv::imread(imagePath);
        if (image.empty()) {
            throw std::runtime_error("Nie można otworzyć pliku: " + imagePath);
        }

        // YOLOv8 ONNX zwykle przyjmuje rozmiar 640x640 – zależnie od wersji
        // Dopasuj wymiary blobu do formatu Twojego modelu
        cv::Mat blob = cv::dnn::blobFromImage(
            image,
            1.0 / 255.0,        // skalowanie
            cv::Size(640, 640), // rozmiar wejściowy sieci
            cv::Scalar(0,0,0),  // średnia do odjęcia
            true,               // swapRB
            false               // crop
        );

        net_.setInput(blob);
        cv::Mat output = net_.forward();  
        // Dla YOLOv8 w ONNX otrzymujemy często macierz Nx(85 lub 7?), w zależności od wersji

        std::vector<Detection> detections;
        parseDetections(output, image.size(), detections);

        // Filtrowanie TYLKO na klasę o ID=2 (car)
        std::vector<Detection> cars;
        for (const auto& det : detections) {
            if (det.classId == 2) { // ID=2 dla 'car' w COCO
                cars.push_back(det);
            }
        }
        return cars;
    }

    // Metoda do rysowania wykryć na obrazie (analogicznie do detect_and_draw_cars)
    void detectAndDrawCars(const std::string& imagePath,
                           const std::string& outputPath = "output.jpg")
    {
        cv::Mat image = cv::imread(imagePath);
        if (image.empty()) {
            throw std::runtime_error("Nie można otworzyć pliku: " + imagePath);
        }

        // Wykryj wszystkie obiekty (nie tylko samochody)
        cv::Mat blob = cv::dnn::blobFromImage(
            image, 1.0/255.0, cv::Size(640,640),
            cv::Scalar(), true, false
        );
        net_.setInput(blob);
        cv::Mat output = net_.forward();

        // Parsujemy wszystkie detekcje
        std::vector<Detection> detections;
        parseDetections(output, image.size(), detections);

        // Rysujemy tylko obiekty, które zostały poprawnie wykryte
        for (const auto& det : detections) {
            // Możesz też dodać warunek: if (det.classId == 2)
            cv::rectangle(image, det.box, cv::Scalar(0,255,0), 2);

            // Tekst z ID klas i pewnością
            std::string label = "ID=" + std::to_string(det.classId) +
                                " conf=" + std::to_string(det.confidence);
            cv::putText(image, label, 
                        cv::Point(det.box.x, det.box.y - 5),
                        cv::FONT_HERSHEY_SIMPLEX, 0.5,
                        cv::Scalar(0,255,0), 1);
        }

        // Zapis i wyświetlenie obrazu
        cv::imwrite(outputPath, image);
        std::cout << "Zapisano obraz z detekcjami do: " << outputPath << std::endl;

        cv::imshow("Detekcja samochodów (C++)", image);
        cv::waitKey(0);
        cv::destroyAllWindows();
    }

private:
    cv::dnn::Net net_;

    // Funkcja pomocnicza do parsowania wyników YOLOv8
    // Uwaga: format wyjścia może się różnić w zależności od wersji YOLO
    void parseDetections(const cv::Mat& output, 
                         const cv::Size& imageSize, 
                         std::vector<Detection>& outDetections,
                         float confThreshold = 0.4,    // próg pewności
                         float iouThreshold  = 0.45)   // próg IoU do NMS
    {
        // W wielu modelach YOLOv8 ONNX output ma wymiary [batch, N, 85]
        // Gdzie:
        //   - N to liczba anchorów/propozycji
        //   - 85 to [cx, cy, w, h, conf, p0, p1, ..., p79] (dla 80 klas COCO)
        // Trzeba to potwierdzić w dokumentacji lub obserwując wymiary matrycy output.

        // 1) Zamiana na tablicę float
        const float* data = (float*)output.data;
        int rows = output.size[1];   // N
        int cols = output.size[2];   // 85 (lub inna liczba)

        std::vector<cv::Rect> boxes;
        std::vector<float> confidences;
        std::vector<int> classIds;

        for (int i = 0; i < rows; ++i) {
            float confidence = data[i * cols + 4];  // to jest conf obiektu
            if (confidence < confThreshold) {
                continue;
            }
            // Znajdź klasę z najwyższym prawdopodobieństwem
            float maxProb = 0.0f;
            int   maxClassId = -1;

            for (int c = 5; c < cols; ++c) {
                float classProb = data[i * cols + c];
                if (classProb > maxProb) {
                    maxProb = classProb;
                    maxClassId = c - 5;
                }
            }
            float score = confidence * maxProb;
            if (score < confThreshold) {
                continue;
            }

            // Pozycja (cx, cy, w, h) w skali [0..1], 
            // o ile model tak generuje (dla YOLO to zazwyczaj [0..1])
            float cx = data[i * cols + 0];
            float cy = data[i * cols + 1];
            float w  = data[i * cols + 2];
            float h  = data[i * cols + 3];

            // Przeliczenie na piksele
            int x = static_cast<int>((cx - 0.5f * w) * imageSize.width);
            int y = static_cast<int>((cy - 0.5f * h) * imageSize.height);
            int width  = static_cast<int>(w * imageSize.width);
            int height = static_cast<int>(h * imageSize.height);

            boxes.push_back(cv::Rect(x, y, width, height));
            confidences.push_back(score);
            classIds.push_back(maxClassId);
        }

        // 2) Non-Maximum Suppression (NMS) – usuwa duplikaty/zbliżone bboxy
        std::vector<int> indices;
        cv::dnn::NMSBoxes(boxes, confidences, confThreshold, iouThreshold, indices);

        for (int idx : indices) {
            Detection det;
            det.box       = boxes[idx];
            det.confidence= confidences[idx];
            det.classId   = classIds[idx];
            outDetections.push_back(det);
        }
    }
};

// ---------------------- EXAMPLE USAGE ----------------------

int main()
{
    try {
        // 1) Inicjalizacja CarCounter z plikiem ONNX
        CarCounter counter("yolov8n.onnx");

        // 2) Detekcja samochodów na obrazie
        std::string inputImage = "test.jpg";
        auto cars = counter.getCarDetections(inputImage);
        std::cout << "Wykryto samochodów: " << cars.size() << std::endl;
        for (size_t i = 0; i < cars.size(); i++) {
            const auto& c = cars[i];
            std::cout << "Car #" << (i+1)
                      << " box=(" << c.box.x << "," << c.box.y 
                                  << "," << c.box.width << "," << c.box.height << ")"
                      << " conf=" << c.confidence
                      << std::endl;
        }

        // 3) (Opcjonalnie) Rysowanie detekcji
        counter.detectAndDrawCars(inputImage, "output.jpg");
    }
    catch (const std::exception& e) {
        std::cerr << "Błąd: " << e.what() << std::endl;
    }
    return 0;
}
