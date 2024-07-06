import cv2
import numpy as np

def Sobel(s):
    sobel_x = cv2.Sobel(s, cv2.CV_64F, 1, 0, ksize=3)     # Applying Sobel filter for horizontal edges
    sobel_y = cv2.Sobel(s, cv2.CV_64F, 0, 1, ksize=3)     # Applying Sobel filter for vertical edges
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2) # Combining Results to Obtain Magnitude of Gradient 
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8) # Adjusting intensity
    return gradient_magnitude


image = cv2.imread(r"D:\CV and Drones\kalam.jpeg")     # Reading an Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # Converting it into grayscale 

edge_detected_image=Sobel(gray_image)

cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', edge_detected_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
