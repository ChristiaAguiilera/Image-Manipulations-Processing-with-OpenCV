# Image-Manipulations-Processing-with-OpenCV  

This repository details the process for using OpenCV correctly with Python, which will help us process data using the OpenCV library. It describes the use of some functions according to their usage, with their respective parameters and codes.

## Pixel arithmetic’s

When we see a color image on a screen, our eyes perceive millions of colors. However, for OpenCV, a color image is nothing more than a three-layered sandwich of mathematical matrices. Each pixel in the image is formed by mixing the three primary colors of light: Red, Green, and Blue (RGB). "Channel decomposition" is literally separating that sandwich into its three individual slices.
```python 
import cv2
import numpy as np

#1. Upload image
img = cv2.imread(r'F:\AIROS CLUB\imagen.jpg')
cv2.imshow('imagen.jpg', img)
cv2.waitKey(0)

# 2. Create an array of the same size filled with a scalar value (e.g., 50)
# This will allow us to add or subtract brightness uniformly
M = np.ones(img.shape, dtype="uint8") * 50

# --- SUM (Increase Brightness) ---
# cv2.add sums and "saturates" to 255 (does not roll back to 0)
sumada = cv2.add(img, M)
cv2.imshow("Mas Brillo (Suma)", sumada)

# --- SUBTRACTION (Darken) ---
# cv2.subtract subtracts and sets to 0 if the result is negative
restada = cv2.subtract(img, M)
cv2.imshow("Menos Brillo (Resta)", restada)

# --- MULTIPLICATION (Contrast) ---
# Multiplying by 1.5 greatly increases contrast
multiplicada = cv2.multiply(img, np.array([1.5]))
cv2.imshow("Contraste (Multiplicacion)", multiplicada)

# --- BLENDING (Mixing two images) ---
# We need a second image of the SAME SIZE as the first.
# If you don't have another one, we'll create a solid gray image for the example.
img2 = np.full(img.shape, 150, dtype="uint8") 

# Formula: (img * 0.7) + (img2 * 0.3) + 0
mezcla = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
cv2.imshow("Mezcla (Blending)", mezcla)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Geometric Transformations 

Antes de transformar, se debe entender que una imagen para la computadora es un plano cartesiano de píxeles. El origen (0,0) está en la esquina superior izquierda y cada transformación es, en esencia, mover un píxel de una coordenada (x, y) a una nueva coordenada (x', y'). Algunos tipos de transformaciones son  translation, rotation, resizing, flipping and cropping.
La función **cv2.warpAffine()** es el motor principal en OpenCV para ejecutar estas transformaciones. Esta función recibe la imagen original y la matriz de transformación específica calculada previamente (por ejemplo, mediante **cv2.getRotationMatrix2D)**. Su trabajo es aplicar la multiplicación matricial a cada píxel de la imagen.
For this examples have two categories: Basic Image Manipulations and Geometric Transformations.

```python
import cv2
import numpy as np

#Upload image
img = cv2.imread(r'F:\AIROS CLUB\imagen.jpg')
alto, ancho = img.shape[:2] # We obtain dimensions for the transformations
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
    50,   # up
    50, # down
    50, # left
    50, # right
    cv2.BORDER_CONSTANT,
    value=[0,0,0])
cv2.imshow("Con borde", borde)
cv2.waitKey(0)


#Geometric Transformations

# ROTATION
# 1. Define the center of rotation, the angle (45°), and the scale (1.0)
centro = (ancho // 2, alto // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, 45, 1.0)
# 2. Apply the affine transformation
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

```
## Pixel Fundamentals & Color 

Each pixel in an image is made up of a mixture of three primary colors of light: Red, Green, and Blue (RGB). "Channel decomposition" is literally separating that sandwich into its three individual slices. While the entire tech world uses the RGB (Red, Green, Blue) format, OpenCV reads images in reverse: in BGR (Blue, Green, Red) format. This is due to a historical reason related to how older cameras delivered data. Therefore, when we decompose an image in OpenCV, the first channel we get is Blue, the second is Green, and the third is Red.

There are two ways to implement color segmentation:
- **Native method:**  The function **cv2.split(image)** splits the image and returns a tuple with the three channels (b, g, r). This is highly readable for educational purposes.
- **NumPy slicing:** In production environments, direct array indexing is recommended (e.g., **blue_channel = image[:, :, 0]**), since NumPy slicing avoids memory reallocation and reduces computational cost.


```pytohn
import cv2

# 1. Load the image
img = cv2.imread(r'F:\AIROS CLUB\frutas.jpg')
cv2.imshow('frutas.jpg', img)
cv2.waitKey(0)

# 2. Split the image (Remember: OpenCV uses BGR, not RGB)
b, g, r = cv2.split(img)

# If you print the dimensions of one of the channels, you'll see that it no longer has the "3" at the end.

# 3. Display the blue channel (it will be displayed in black and white/grayscale)
cv2.imshow('Blue Intensity', b)
cv2.imshow('Green Intensity', g)
cv2.imshow('Red Intensity', r)
cv2.waitKey(0)
cv2.destroyAllWindows()


# NumPy slicing:
# import cv2
# 1. Load the image
img = cv2.imread(r'F:\AIROS CLUB\frutas.jpg')
cv2.imshow('Original Image', img)                    
cv2.waitKey(0)

# 2. Channel Splitting using Slicing
# OpenCV uses BGR format: index 0 is Blue, 1 is Green, 2 is Red
# Syntax: img[height, width, channel]
blue_channel  = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel   = img[:, :, 2]

# Note: If you check blue_channel.shape, it will be (height, width) 
# without the '3' because it is now a 2D grayscale intensity map.

# 3. Display individual channel intensities
cv2.imshow('Blue Intensity', blue_channel)
cv2.imshow('Green Intensity', green_channel)
cv2.imshow('Red Intensity', red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
## END 

This concludes our introduction to using OpenCV for Python. We hope this text has served its purpose and is useful for improving your understanding of the library.
att: Christian Aguilera
