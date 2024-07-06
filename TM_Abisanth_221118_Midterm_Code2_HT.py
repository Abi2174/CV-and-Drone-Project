import cv2
import numpy as np

def hough_line(s):
    
    image = cv2.imread(s)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Edge detected image using canny method
    edge_detected_img = cv2.Canny(gray_image, 50, 150, apertureSize=3)
    # Applying the  Hough Line Transform
    lines_hough = cv2.HoughLines(edge_detected_img, 1, np.pi / 180, threshold=100)
    # Superposing  the hough lines on the original image
    copy_image = image.copy()

    if lines_hough is not None:
        for line in lines_hough:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            
            # Drawing the Hough line on the image
            cv2.line(copy_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    
    cv2.imshow('Original Image', image)
    cv2.imshow('Hough Line Image', copy_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"D:\CV and Drones\building_2.jpg"
hough_line(image_path)
