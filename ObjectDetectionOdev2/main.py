import cv2
import numpy as np

def detect_red_objects(frame):
    # Görüntüyü HSV renk uzayına dönüştür
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk için alt ve üst HSV sınırları
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Kırmızı renk aralığını maskeleme
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Görüntüdeki kırmızı renkli nesneleri belirleme
    red_objects = cv2.bitwise_and(frame, frame, mask=red_mask)

    return red_objects

# Kamera bağlantısını başlatma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kırmızı nesneleri tespit et
    red_objects = detect_red_objects(frame)

    # Kırmızı nesneleri göster
    cv2.imshow("Red Objects", red_objects)

    # Q tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
