import os
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

folder_path = r"C:\\Users\\Kasia\\OV_notebooks\\openvino_env\\Scripts\\openvino_notebooks\\notebooks\\000-erytrocyty\\data\\rav"
source_file = "photo_06.png"
img_path = os.path.join(folder_path, source_file)

def rgb_to_cmyk(r, g, b):
    r_prime = r / 255.0
    g_prime = g / 255.0
    b_prime = b / 255.0

    k = 1 - max(r_prime, g_prime, b_prime)
    c = (1 - r_prime - k) / (1 - k) if (1 - k) != 0 else 0
    m = (1 - g_prime - k) / (1 - k) if (1 - k) != 0 else 0
    y = (1 - b_prime - k) / (1 - k) if (1 - k) != 0 else 0

    return c, m, y, k

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
    range_red[0] = red_slider_min.val
    range_red[1] = red_slider_max.val
    range_green[0] = green_slider_min.val
    range_green[1] = green_slider_max.val
    range_blue[0] = blue_slider_min.val
    range_blue[1] = blue_slider_max.val
    
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
    
    ax.imshow(cv.cvtColor(binary_image_gray, cv.COLOR_BGR2RGB))
    fig.canvas.draw_idle()

# Tworzenie interaktywnego wykresu z suwakami
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# Ustawienia dla suwaka czerwonego (minimalna wartość)
red_slider_min_ax = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
red_slider_min = Slider(red_slider_min_ax, 'Red Min', 0, 255, valinit=range_red[0], valstep=1)

# Ustawienia dla suwaka czerwonego (maksymalna wartość)
red_slider_max_ax = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
red_slider_max = Slider(red_slider_max_ax, 'Red Max', 0, 255, valinit=range_red[1], valstep=1)

# Ustawienia dla suwaka zielonego (minimalna wartość)
green_slider_min_ax = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
green_slider_min = Slider(green_slider_min_ax, 'Green Min', 0, 255, valinit=range_green[0], valstep=1)

# Ustawienia dla suwaka zielonego (maksymalna wartość)
green_slider_max_ax = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
green_slider_max = Slider(green_slider_max_ax, 'Green Max', 0, 255, valinit=range_green[1], valstep=1)

# Ustawienia dla suwaka niebieskiego (minimalna wartość)
blue_slider_min_ax = plt.axes([0.2, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')
blue_slider_min = Slider(blue_slider_min_ax, 'Blue Min', 0, 255, valinit=range_blue[0], valstep=1)

# Ustawienia dla suwaka niebieskiego (maksymalna wartość)
blue_slider_max_ax = plt.axes([0.2, 0.3, 0.65, 0.03], facecolor='lightgoldenrodyellow')
blue_slider_max = Slider(blue_slider_max_ax, 'Blue Max', 0, 255, valinit=range_blue[1], valstep=1)

update(None)
# Połączenie suwaków z funkcją aktualizacji
red_slider_min.on_changed(update)
red_slider_max.on_changed(update)
green_slider_min.on_changed(update)
green_slider_max.on_changed(update)
blue_slider_min.on_changed(update)
blue_slider_max.on_changed(update)

plt.show()