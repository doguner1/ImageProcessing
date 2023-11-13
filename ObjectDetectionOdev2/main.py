import cv2
import numpy as np

# Kamerayı başlat
kamera = cv2.VideoCapture(0)

"""
Telefondan kamera kullanmak için

# DroidCam uygulaması olabilir..
ip_address = "192.168...."
port = 4747

#Görüntü Çağırma kodu şöyle değişir:
cv2.VideoCapture(f"http://{ip_address}:{port}/video")
"""

while True:
    # Kameradan görüntü al
    ret, kare = kamera.read()
    cv2.imshow('Orjinal Kare',kare)

    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Yeşil renk
    lower_green = np.array([36, 25, 25])
    upper_green = np.array([70, 255, 255])
    mask1 = cv2.inRange(hsv, lower_green, upper_green)

    # Mavi renk
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([120, 255, 255])
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

    # Yeşil ve mavi renk alanlarını birleştir
    mask = mask1 + mask2

    # Maskı burada siyah ve beyaz yapıyoruz
    kare[mask > 0] = [0, 0, 0]

    # Görüntüyü göster
    cv2.imshow('Renk Tespiti', kare)

    # Çıkış yapmak için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
kamera.release()
cv2.destroyAllWindows()
