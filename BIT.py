# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tenemos 4 tipos: (Operaciones logicas)
# cv2.bitwise_and(img1, img2 , mask)  |  cv2.bitwise_or()  |  cv2.bitwise_xor()  |  cv2.bitwise_not()

# IMAGENES
img1 = cv2.imread('img1.png', 0)
img2 = cv2.imread('img2.png', 0)

# OPERACION AND
imgand = cv2.bitwise_and(img1, img2, mask = None)

# OPERACION OR
imgor = cv2.bitwise_or(img1, img2, mask = None)

# OPERACION XOR
imgxor = cv2.bitwise_xor(img1, img2, mask = None)


# Mostramos Imagenes
fig = plt.figure()

# IMAGEN 1
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(img1, cmap="gray")
ax1.set_title("IMAGEN 1")

# IMAGEN 2
ax2 = fig.add_subplot(2,3,4)
ax2.imshow(img2, cmap="gray")
ax2.set_title("IMAGEN 2")

# IMAGEN AND
ax3 = fig.add_subplot(2,3,2)
ax3.imshow(imgand, cmap="gray")
ax3.set_title("IMAGEN AND")

# IMAGEN OR
ax4 = fig.add_subplot(2,3,3)
ax4.imshow(imgor, cmap="gray")
ax4.set_title("IMAGEN OR")

# IMAGEN XOR
ax5 = fig.add_subplot(2,3,5)
ax5.imshow(imgxor, cmap="gray")
ax5.set_title("IMAGEN XOR")

# APLICACION CON IMG
imglogo = cv2.imread('logo.png')
imgback = cv2.imread('fondo.png')

# CORRECCION DE COLOR
imglogo = cv2.cvtColor(imglogo, cv2.COLOR_BGR2RGB)
imgback = cv2.cvtColor(imgback, cv2.COLOR_BGR2RGB)

# CREAMOS UNA MASCARA
logogray = cv2.cvtColor(imglogo, cv2.COLOR_RGB2GRAY)
_, imgmask = cv2.threshold(logogray, 127, 255, cv2.THRESH_BINARY)

# MASCARA INVERTIDA
imgmaskinv = cv2.bitwise_not(imgmask)

# REALIZAMOS OPERACIONES
imgapp1 = cv2.bitwise_and(imglogo, imgback, mask = imgmask)

imgapp2 = cv2.bitwise_and(imglogo, imglogo, mask = imgmaskinv)

imgapp3 = cv2.subtract(imgback, imgapp2)

# Mostramos Imagenes
fig1 = plt.figure()

# IMAGEN 1
ax11 = fig1.add_subplot(3,3,1)
ax11.imshow(imglogo)
ax11.set_title("IMAGEN 1")

# IMAGEN 2
ax22 = fig1.add_subplot(3,3,4)
ax22.imshow(imgback)
ax22.set_title("IMAGEN 2")

# IMAGEN MASK
ax33 = fig1.add_subplot(3,3,2)
ax33.imshow(imgmask, cmap="gray")
ax33.set_title("IMAGEN MASK")

# IMAGEN MASK INVERTIDA
ax44 = fig1.add_subplot(3,3,3)
ax44.imshow(imgmaskinv, cmap='gray')
ax44.set_title("IMAGEN MASK INV")

# IMAGEN AND
ax44 = fig1.add_subplot(3,3,5)
ax44.imshow(imgapp1)
ax44.set_title("IMAGEN AND")

# IMAGEN AND 2
ax44 = fig1.add_subplot(3,3,6)
ax44.imshow(imgapp2)
ax44.set_title("IMAGEN AND 2")

# IMAGEN ADD
ax44 = fig1.add_subplot(3,3,8)
ax44.imshow(imgapp3)
ax44.set_title("IMAGEN ADD")



plt.show()
