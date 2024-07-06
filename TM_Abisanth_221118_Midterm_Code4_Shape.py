import cv2

def get_shape_name(data):

    sides = len(data)
    if sides == 3:
        return "Triangle"
    elif sides == 4:
        x, y, w, h = cv2.boundingRect(data)  # x,y represent top left corner coordinates and w,h represent width and height
        edge_ratio = (float(w)+float(h))/ (2*float(w))
        if 0.95 <= edge_ratio <= 1.05:
            return "Square"
        elif 1.3 >= edge_ratio >= 0.7:
            return "Rectangle"
        else:
            return "Quadrilateral"
        
    elif sides == 5:
        return "Pentagon"
    elif sides == 6:
        return "Hexagon"
    elif sides == 7:
        return "Heptagon"
    elif sides == 8:
        return "Octagon"
    elif sides == 9:
        return "Nonagon"
    
def shape(s):

    image = cv2.imread(s)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edge_detected_img = cv2.Canny(blurred_image, 50, 150)
    
    contours, _ = cv2.findContours(edge_detected_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Sorting the contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    Contour_image = image.copy()
    
    # Iterate over all the contours
    for i, contour in enumerate(contours):
        # Findind the center of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])

            # Marking centre of largest and second largest
            if i < 2:
                cv2.circle(Contour_image, (center_x, center_y), 5, (255, 0, 0), -1)

            # Finding the shape from edges
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            shape_name = get_shape_name(approx)

            # Write the name of the shape above all detected shapes
            cv2.putText(Contour_image, shape_name, (center_x - 30, center_y - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 100,250), 2)

            # Marking the largest and second largest shapes
            if i == 0:
                cv2.putText(Contour_image, "Largest-1", (center_x - 30, center_y - 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            elif i == 1:
                cv2.putText(Contour_image, "Largest-2", (center_x - 30, center_y - 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow('Original Image', image)
    cv2.imshow('Shape with name', Contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r"D:\CV and Drones\color_m.png"
shape(image_path)
