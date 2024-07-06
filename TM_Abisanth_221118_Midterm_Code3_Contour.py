import cv2
import numpy as np

def colour(s):
    
    image = cv2.imread(s)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # setting up RGB value range to get desired color
    lower_limit = np.array([100, 0, 0], dtype=np.uint8)
    upper_limit = np.array([255,180,150], dtype=np.uint8)

    suitable_img = cv2.inRange(rgb_image, lower_limit, upper_limit)
    contours, _ = cv2.findContours(suitable_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    copy_image = image.copy()
    cv2.drawContours(copy_image, contours, -1, (255,0, 0), 2)  # RED color contours

    cv2.imshow('Original Image', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2.imshow('Selective Contour', cv2.cvtColor(copy_image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"D:\CV and Drones\color2.jpg"
colour(image_path)
