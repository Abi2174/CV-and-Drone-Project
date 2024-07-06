import cv2
import numpy as np
def ig_filter(s):
    image_float = s.astype(np.float32)
    # Reducing the brightness to 0.5 of its initial value
    brightness_factor = 0.5
    brightness_red = np.clip(image_float * brightness_factor, 0, 255).astype(np.uint8)
    # Increasing the contrast to 1.5 of its initial value
    contrast_factor=1.5
    contrast_img=np.clip(brightness_red  * contrast_factor, 0, 255).astype(np.uint8)
    # Increasing the saturation of the image to 1.5 of its initial value
    hsv_image = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV) # Converting the image from the BGR color space to the HSV (Hue, Saturation, Value) color space
    saturation_factor = 1.5
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)

    insta_img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return insta_img


image=cv2.imread(r"D:\CV and Drones\S1.png")
insta_img=ig_filter(image)
cv2.imshow("Original Image",image)
cv2.imshow("Insta Filtered Image",insta_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    

