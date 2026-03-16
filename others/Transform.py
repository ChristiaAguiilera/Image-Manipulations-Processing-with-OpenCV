import cv2
import numpy as np

#Upload image
img = cv2.imread(r'F:\AIROS CLUB\imagen.jpg')
alto, ancho = img.shape[:2] # Obtenemos dimensiones para las transformaciones
#display image in window
cv2.imshow('imagen.jpg', img)
cv2.waitKey(0) #It makes the window stay open 

#Basic Image Manipulations
# CROPPING (recorte)
recorte = img[50:300, 100:400] 
cv2.imshow('Recorte', recorte)
cv2.waitKey(0)

# FLIPPING (Volteo)
# Parameter 1 indicates horizontal
# Parameter 0 indicates vertical
# Parameter -1 indicates both
img2 = cv2.flip(img, -1)
cv2.imshow('Flipped', img2)
cv2.waitKey(0)

# PADDING (relleno)
borde = cv2.copyMakeBorder(
    img,
    50,   # arriba
    50,   # abajo
    50,   # izquierda
    50,   # derecha
    cv2.BORDER_CONSTANT,
    value=[0,0,0])
cv2.imshow("Con borde", borde)
cv2.waitKey(0)


#Geometric Transformations
# ROTATION (rotacion)
# 1. Definir el centro de rotación, el ángulo (45°) y la escala (1.0)
centro = (ancho // 2, alto // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, 45, 1.0)
# 2. Aplicar la transformación afín
rotacion = cv2.warpAffine(img, matriz_rotacion, (ancho, alto))
cv2.imshow('Rotacion', rotacion)
cv2.waitKey(0)

# TRASLATION (traslacion)
M_traslacion = np.float32([[1, 0, 100], [0, 1, 50]]) 
traslacion = cv2.warpAffine(img, M_traslacion, (ancho, alto))
cv2.imshow('Traslacion', traslacion)
cv2.waitKey(0)

# RESIZING (redimensionamiento)
resizing = cv2.resize(img, (500, 300), interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resizing', resizing)
cv2.waitKey(0)





