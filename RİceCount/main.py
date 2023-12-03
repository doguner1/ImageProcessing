import cv2
import numpy as np

# Kamerayı başlat.
# DroidCam kullanıldı.
ip_address = "192.168.1.153"
port = 4747
cap = cv2.VideoCapture(f"http://{ip_address}:{port}/video") #-> Telefon Kamerasından Görüntü Alma

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #-> Kameradan alınan görüntü griye dönüştürüldü

  
    _, threshold = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY) 
    #Eşik ayarı yapıldığı alan. Burada 120,255 alanında gece lambasının ışığını prinçmiş gibi algıladığından değeri yüksettim.


    # Morfolojik işlemler (örneğin, açılma işlemi)
    kernel = np.ones((4, 4), np.uint8)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    #Morfolojik işlemler, görüntüdeki nesnelerin şeklini ve boyutunu değiştirmek için kullanılır


    # Bağlantılı bileşen analizi
    connectivity = 8
    output = cv2.connectedComponentsWithStats(opening, connectivity, cv2.CV_32S)
    num_labels = output[0]
    # İlk etiketlenmiş nesne dışındaki arka planı çıkart
    stats = output[2][1:]  # İlk nesne dışındaki istatistikler
    centroids = output[3][1:]  # İlk nesne dışındaki merkezler

    # Pirinç sayısını görsel olarak görüntüye ekle
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(opening, f"Pirinc Sayisi: {len(stats)}", (40, 40), font, 1, (255,0,0), 2, cv2.LINE_AA)
    """
    Yukardaki kod opening penceresinde
    Konumu-font büyüklüğü-renki-kalınlığı
    ayarlanarak metin eklemiştir
    """

    # Görüntüleri göster
    cv2.imshow('Processed', opening)
    cv2.imshow('Original', frame)
    

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()

