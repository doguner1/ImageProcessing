import cv2

# Resim adı
image_name = "/Users/dogugnr/Documents/Yazılım/PythonPyCharm/A.jpg"
# Görüntüyü oku
img = cv2.imread(image_name)

# Görüntüyü gri tonlamaya dönüştür
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kanalları düzleştir
# Kanalların histogram ve normalleştirilmiş histogramını elde etmek için hist işlevini kullanın
size_y = img.shape[0]  # şekli al
size_x = img.shape[1]

flattened = img.reshape([size_x * size_y])  # Matrisleri düzleştir

# pylot'u içe aktar
from matplotlib import pyplot as plt

# 256 binli histogram oluştur ve göster
rhist, _, _ = plt.hist(flattened, bins=256)  #, log=True)
plt.show()

# 32 binli histogram oluştur ve göster
rhist, _, _ = plt.hist(flattened, bins=32)  #, log=True)
plt.show()

# 8 binli histogram oluştur ve göster
rhist, _, _ = plt.hist(flattened, bins=8)  #, log=True)
plt.show()