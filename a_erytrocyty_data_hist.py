import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

folder_path = r"C:\Users\Kasia\workspace\lab_6\bird_miniatures"
source_file = "E0206_TR0001_OB0020_T01_M10.jpg"
img_path = os.path.join(folder_path, source_file)

def draw_histogram(image, title):
    # Oblicz histogramy dla kanałów RGB
    hist_red = cv.calcHist([image], [0], None, [256], [0, 256])
    hist_green = cv.calcHist([image], [1], None, [256], [0, 256])
    hist_blue = cv.calcHist([image], [2], None, [256], [0, 256])

    # Rysuj histogramy na jednym wykresie
    plt.plot(hist_red, color='red', label='Red')
    plt.plot(hist_green, color='green', label='Green')
    plt.plot(hist_blue, color='blue', label='Blue')

    plt.title(title)
    plt.xlabel('Wartość piksela')
    plt.ylabel('Ilość pikseli')
    plt.xlim([0, 256])
    plt.legend()
    plt.show()
    
# Sprawdź, czy plik istnieje
assert os.path.exists(img_path), "File could not be read, check with os.path.exists()"

# Wczytaj obraz
img = cv.imread(img_path, cv.IMREAD_COLOR)

# Sprawdź, czy obraz został poprawnie wczytany
assert img is not None, "File could not be read, check with os.path.exists()"

# Podziel obraz na kanały kolorów
b, g, r = cv.split(img)

# Ustaw początkowe zakresy wartości dla progów binaryzacji dla kanałów czerwonego, zielonego i niebieskiego
# 195, 146, 208, 196, 170, 217 -> samples of color of an erythrocyte
range_red = [150, 255] 
range_green = [200, 255]
range_blue = [130, 230]
# Binaryzacja kanałów czerwonego, zielonego i niebieskiego na podstawie zakresów wartości
_, thresh_r = cv.threshold(r, *range_red, cv.THRESH_BINARY)
_, thresh_g = cv.threshold(g, *range_green, cv.THRESH_BINARY)
_, thresh_b = cv.threshold(b, *range_blue, cv.THRESH_BINARY)

# Połączenie binaryzowanych kanałów
binary_image = cv.bitwise_and(thresh_r, cv.bitwise_and(thresh_g, thresh_b))

# Konwersja na obraz czarno-biały
binary_image[binary_image > 0] = 255  # Wszystkie wartości różne od zera ustawiane są na 255

# Konwersja na obraz w odcieniach szarości
binary_image = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR)

def invert_colors(image):
    return cv.bitwise_not(image)

# Funkcja do aktualizacji obrazu po zmianie wartości slidera
def update(val):
    
    _, thresh_r = cv.threshold(r, *range_red, cv.THRESH_BINARY)
    _, thresh_g = cv.threshold(g, *range_green, cv.THRESH_BINARY)
    _, thresh_b = cv.threshold(b, *range_blue, cv.THRESH_BINARY)
    
    # Połączenie binaryzowanych kanałów
    binary_image = cv.bitwise_and(thresh_r, cv.bitwise_and(thresh_g, thresh_b))
    
    # Konwersja na obraz czarno-biały
    binary_image[binary_image > 0] = 255
    
    # Inwersja kolorów
    # binary_image = invert_colors(binary_image)
    
    # Konwersja na obraz w odcieniach szarości
    binary_image_gray = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR)
    

# Tworzenie interaktywnego wykresu z suwakami

update(None)
# Połączenie suwaków z funkcją aktualizacji


color_img = cv.imread(img_path, cv.IMREAD_COLOR)


# Rysuj histogramy dla kanałów RGB
draw_histogram(color_img, 'Histogram kolorów RGB')