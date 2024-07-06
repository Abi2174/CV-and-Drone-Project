import cv2
import numpy as np

def flag_generate():
    
    flag = np.ones((600, 600, 3)) * 255

    def ashok_chakra():
        cv2.circle(flag, (300,300), 100, (0,0,255), 1)

        # Draw the spokes of the chakra
        for t in range(0, 360, 15):
            x1 = int(300 + 100*np.cos(np.deg2rad(t)))
            y1 = int(300 + 100*np.sin(np.deg2rad(t)))
            cv2.line(flag, (300,300), (x1,y1), (0,0,255), 1)

    flag[0:200, 0:600] = [255, 165, 0]
    flag[200:400, 0:600] = [255, 255, 255]
    flag[400:600, 0:600] = [0, 128, 0]
  
    ashok_chakra()
    img_float32 = np.uint8(flag)
    indian_flag = cv2.cvtColor(img_float32, cv2.COLOR_RGB2BGR)
    return indian_flag


def rotate_image(img, angle_degrees):

    height, width, _ = img.shape
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle_degrees, 1)
    rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
   
    return rotated_image
 
def unskew(s):

    img = cv2.imread(s)
    flag = flag_generate()
    num = 0
    num2 = 0
    vertical_midline = img[:, 299, :]
    horizontal_midline = img[299, :, :]
    
    while (not((vertical_midline[num] == np.array([52, 153, 255])).all() or (vertical_midline[num] == np.array([255, 255, 255])).all() or (vertical_midline[num] == np.array([1, 128, 0])).all())):
            num+=1
            
    if (vertical_midline[num] == np.array([52, 153, 255])).all():
        final_img = rotate_image(flag, 0)
    if (vertical_midline[num] == np.array([52, 153, 255])).all():
        final_img = rotate_image(flag, 180)
    else:
        while (not((horizontal_midline[num2] == np.array([52, 153, 255])).all() or (horizontal_midline[num2] == np.array([1, 128, 0])).all())):
            num2+=1
        if (horizontal_midline[num2] == np.array([52, 153, 255])).all():
            final_img = rotate_image(flag, 90)
        elif (horizontal_midline[num2] == np.array([1, 128, 0])).all():
            final_img = rotate_image(flag, 270)

    cv2.imshow("Original Image", img)
    cv2.imshow("Unskewed Image", final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
image = flag_generate()
s = r"D:\CV and Drones\skew_1.jpg"
unskew(s)

    
    
