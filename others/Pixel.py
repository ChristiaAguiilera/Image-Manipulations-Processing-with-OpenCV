import cv2
import numpy as np

#1)Upload image
img = cv2.imread(r'F:\AIROS CLUB\imagen.jpg')
cv2.imshow('imagen.jpg', img)
cv2.waitKey(0)

# 2. Crear una matriz del mismo tamaño llena de un valor escalar (ej. 50)
# Esto nos servirá para sumar o restar brillo de forma uniforme
M = np.ones(img.shape, dtype="uint8") * 50

# --- SUMA (Aumentar Brillo) ---
# cv2.add suma y "satura" en 255 (no da la vuelta a 0)
sumada = cv2.add(img, M)
cv2.imshow("Mas Brillo (Suma)", sumada)

# --- RESTA (Oscurecer) ---
# cv2.subtract resta y clava en 0 si el resultado es negativo
restada = cv2.subtract(img, M)
cv2.imshow("Menos Brillo (Resta)", restada)

# --- MULTIPLICACIÓN (Contraste) ---
# Multiplicar por 1.5 aumenta mucho el contraste
multiplicada = cv2.multiply(img, np.array([1.5]))
cv2.imshow("Contraste (Multiplicacion)", multiplicada)

# --- BLENDING (Mezcla de dos imágenes) ---
# Necesitamos una segunda imagen del MISMO TAMAÑO que la primera
# Si no tienes otra, crearemos una imagen gris sólida para el ejemplo
img2 = np.full(img.shape, 150, dtype="uint8") 

# Formula: (img * 0.7) + (img2 * 0.3) + 0
mezcla = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
cv2.imshow("Mezcla (Blending)", mezcla)

cv2.waitKey(0)
cv2.destroyAllWindows()