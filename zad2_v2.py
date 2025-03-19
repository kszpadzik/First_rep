import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "birds_divided.png"
image = cv2.imread(image_path)

# debug purpose
if image is None:
    print("Nie udało się wczytać obrazu. Upewnij się, że ścieżka do pliku jest poprawna.")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Metoda 1: Średnia arytmetyczna kanałów RGB
gray_avg = np.mean(image_rgb, axis=2).astype(np.uint8)

# Metoda 2: Wzór ważony 0.299*R + 0.587*G + 0.114*B
gray_weighted = (
    0.299 * image_rgb[:, :, 0] + 
    0.587 * image_rgb[:, :, 1] + 
    0.114 * image_rgb[:, :, 2]
).astype(np.uint8)

# Wyświetlenie oryginalnego obrazu i wyników obu metod
plt.figure(figsize=(15, 5))

# Oryginalny obraz kolorowy
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Oryginalny obraz (RGB)")
plt.axis("off")

# Obraz w skali szarości - średnia
plt.subplot(1, 3, 2)
plt.imshow(gray_avg, cmap="gray")
plt.title("Szarość - średnia arytmetyczna")
plt.axis("off")

# Obraz w skali szarości - wzór ważony
plt.subplot(1, 3, 3)
plt.imshow(gray_weighted, cmap="gray")
plt.title("Szarość - wzór ważony")
plt.axis("off")

plt.tight_layout()
plt.show()

# Porównanie statystyczne
# Obliczamy różnicę między metodami
difference = np.abs(gray_avg - gray_weighted)
mean_difference = np.mean(difference)

print(f"Średnia różnica między metodami: {mean_difference:.2f}")

# Wyświetlenie mapy różnic
plt.figure(figsize=(8, 6))
plt.imshow(difference, cmap="hot")
plt.title("Różnica między metodami (średnia - ważona)")
plt.colorbar(label="Wartość różnicy")
plt.axis("off")
plt.show()
