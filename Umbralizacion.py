# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestra imagen
img = cv2.imread('monedas.jpg')

# Convertimos a EDG
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creamos una matriz del tamaño de la IMG
matriz = np.ones(gray.shape, dtype='uint8') * 50

# Umbralizamos imagen brillante
# Comando: retval, dst = cv2.threshold(img, tresh(Umbral: debajo = 0, encima = 255), maxval, tipo de umbral)
#                  maxval = TRESH_BINARY o THRESH_BINARY_INV
# Comando:         dst = cv2.adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blocksize)
#                  adaptiveMethod = BORDER_REPLICATE o BORDER_ISOLATE
#                  thresholdType = TRESH_BINARY o THRESH_BINARY_INV

# Aumentamos le brillo de la imagen en GRAY
brillantegray = cv2.add(gray, matriz)

# THRESHOLD

_, imgthresh1 = cv2.threshold(brillantegray, 160, 255, cv2.THRESH_BINARY)

_, imgthresh2 = cv2.threshold(brillantegray, 180, 255, cv2.THRESH_BINARY_INV)

# THRESHOLD ADAPTIVE
imgadaptive1 = cv2.adaptiveThreshold(brillantegray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)


# Disminuimos el brillo en GRAY
oscuragray = cv2.subtract(gray, matriz)

_, imgthresh3 = cv2.threshold(oscuragray, 50, 255, cv2.THRESH_BINARY)

_, imgthresh4 = cv2.threshold(oscuragray, 50, 255, cv2.THRESH_BINARY_INV)

# THRESHOLD ADAPTIVE
imgadaptive2 = cv2.adaptiveThreshold(oscuragray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 7)

# Mostramos Imagenes
fig = plt.figure()
# BRILLANTE
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(brillantegray, cmap="gray")
ax1.set_title("BRILLANTE")

# BRILLANTE THRESH 1
ax3 = fig.add_subplot(2,4,2)
ax3.imshow(imgthresh1, cmap="gray")
ax3.set_title("BRILLANTE THRESH 1")

# BRILLANTE THRESH 2
ax4 = fig.add_subplot(2,4,3)
ax4.imshow(imgthresh2, cmap="gray")
ax4.set_title("BRILLANTE THRESH 2")

# BRILLANTE ADAPTIVE
ax4 = fig.add_subplot(2,4,4)
ax4.imshow(imgadaptive1, cmap="gray")
ax4.set_title("BRILLANTE ADAPTIVE 1")

# OSCURA
ax2 = fig.add_subplot(2,4,5)
ax2.imshow(oscuragray, cmap="gray")
ax2.set_title("OSCURA")

# OSCURA THRESH 1
ax3 = fig.add_subplot(2,4,6)
ax3.imshow(imgthresh3, cmap="gray")
ax3.set_title("OSCURA THRESH 1")

# OSCURA THRESH 2
ax4 = fig.add_subplot(2,4,7)
ax4.imshow(imgthresh4, cmap="gray")
ax4.set_title("OSCURA THRESH 2")

# OSCURA ADAPTIVE
ax4 = fig.add_subplot(2,4,8)
ax4.imshow(imgadaptive2, cmap="gray")
ax4.set_title("OSCURA ADAPTIVE 1")

plt.show()
