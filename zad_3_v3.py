import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def count_birds_in_image(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Nie udało się wczytać obrazu: {image_path}")
        return None

    # Konwersja do skali szarości
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # binaryzacja obrazu
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Liczenie konturów
    bird_count = len(contours)
    
    # Wyświetlenie przetworzonego obrazu z konturami
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Oryginalny obraz")
    plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.title(f"Ptaki zaznaczone (liczba: {bird_count})")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    
    return bird_count

# Funkcja do przetwarzania wszystkich obrazów w folderze
def process_folder(folder_path):
    bird_counts = []
    
    # Iterowanie przez wszystkie pliki w folderze
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            bird_count = count_birds_in_image(image_path)
            
            if bird_count is not None:
                bird_counts.append((filename, bird_count))
                print(f"Obraz: {filename} | Liczba ptaków: {bird_count}")
    
    return bird_counts


if __name__ == "__main__":
    folder_path = r"C:\Users\Kasia\workspace\lab_6\bird_miniatures"
    
    bird_counts = process_folder(folder_path)

    print("\nPodsumowanie:")
    for filename, count in bird_counts:
        print(f"{filename}: {count} ptaków")
