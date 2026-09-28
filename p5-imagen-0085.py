import cv2
#leer la imagen
img = cv2.imread('gato.jpg')
#determinar el tipo de imagen numpy.ndarray
print(type(img))
#mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrar imagen en ventana barra de titulo gato 0085
cv2.imshow('gato.jpg', img)
# tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()