import cv2
import matplotlib.pyplot as plt


def show_histogram(image_path, num_bins=256):
    # Görüntüyü oku
    img = cv2.imread(image_path)

    # Görüntüyü gri tonlamaya dönüştür
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Görüntü boyutlarını al
    size_y = img_gray.shape[0]
    size_x = img_gray.shape[1]

    # Görüntüyü düzleştir
    flattened = img_gray.reshape([size_x * size_y])

    # Histogram oluştur ve göster
    plt.hist(flattened, bins=num_bins)
    plt.title(f"{num_bins}-Bin Histogram")
    plt.xlabel("Pixel Değerleri")
    plt.ylabel("Pixel Sayısı")
    plt.show()


# Resim adı ve isteğe bağlı olarak bin sayısını belirleyerek fonksiyonu çağırma işlemi.
image_name = "/Users/dogugnr/Documents/Yazılım/PythonPyCharm/A.jpg"
show_histogram(image_name, num_bins=256)
show_histogram(image_name, num_bins=32)
show_histogram(image_name, num_bins=8)
