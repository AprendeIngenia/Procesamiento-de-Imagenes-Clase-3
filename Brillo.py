# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestra imagen
img = cv2.imread('monedas.jpg')
imgmat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convertimos a EDG
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creamos una matriz del tamaño de la IMG
matriz = np.ones(gray.shape, dtype='uint8') * 50
matrizrgb = np.ones(img.shape, dtype='uint8') * 50

# Aumentamos el brillo de la imagen en RGB
brillantergb = cv2.add(img, matrizrgb)
brillantergbm = cv2.cvtColor(brillantergb, cv2.COLOR_BGR2RGB)

# Disminuimos el brillo en RGB
oscurargb = cv2.subtract(img, matrizrgb)
oscurargbm = cv2.cvtColor(oscurargb, cv2.COLOR_BGR2RGB)

# Aumentamos le brillo de la imagen en GRAY
brillantegray = cv2.add(gray, matriz)

# Disminuimos el brillo en GRAY
oscuragray = cv2.subtract(gray, matriz)

# Mostramos Imagenes
fig = plt.figure()
# IMAGEN ORIGINAL
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(imgmat)
ax1.set_title("IMAGEN ORIGINAL")

# BRILLANTE RGB
ax3 = fig.add_subplot(2,3,2)
ax3.imshow(brillantergbm)
ax3.set_title("BRILLANTE RGB")

# OSCURA RGB
ax4 = fig.add_subplot(2,3,3)
ax4.imshow(oscurargbm)
ax4.set_title("OSCURA RGB")

# IMAGEN GRAY
ax2 = fig.add_subplot(2,3,4)
ax2.imshow(gray, cmap="gray")
ax2.set_title("ESCALA DE GRISES")

# BRILLANTE GRAY
ax3 = fig.add_subplot(2,3,5)
ax3.imshow(brillantegray, cmap="gray")
ax3.set_title("BRILLANTE EDG")

# OSCURA GRAY
ax4 = fig.add_subplot(2,3,6)
ax4.imshow(oscuragray, cmap="gray")
ax4.set_title("OSCURA EDG")

plt.show()

# Mostramos la imagen
cv2.imshow('IMAGEN BRILLANTE GRAY',brillantegray)
cv2.imshow('IMAGEN OSCURA GRAY',oscuragray)
cv2.imshow('IMAGEN BRILLANTE RGB',brillantergb)
cv2.imshow('IMAGEN OSCURA RGB',oscurargb)
cv2.waitKey(0)