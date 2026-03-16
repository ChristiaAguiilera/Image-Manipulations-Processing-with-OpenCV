import cv2

# 1. Cargamos la imagen
img = cv2.imread(r'F:\AIROS CLUB\frutas.jpg')
cv2.imshow('frutas.jpg', img)                    
cv2.waitKey(0)

# 2. Hacemos el Split (Recuerda: OpenCV usa BGR, no RGB)
b, g, r = cv2.split(img)

# Si imprimes las dimensiones de uno de los canales, verás que ya no tiene el "3" al final

# 3. Mostramos el canal azul (se verá en blanco y negro/escala de grises)
cv2.imshow('Intensidad del Azul', b)
cv2.imshow('Intensidad del Verde', g)
cv2.imshow('Intensidad del Rojo', r)
cv2.waitKey(0)
cv2.destroyAllWindows()