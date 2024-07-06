import numpy as np
import cv2

def draw_axes(image, matrix_coefficients, distortion_coefficients, rvec, tvec, size=30):

    axis_points = np.float32([[0, 0, 0], [size, 0, 0], [0, size, 0], [0, 0, -size]]).reshape(-1, 3)
    image_points, _ = cv2.projectPoints(axis_points, rvec, tvec, matrix_coefficients, distortion_coefficients)
 
    image_points = tuple(map(tuple, image_points.reshape(-1, 2).astype(int)))
   
    cv2.line(image, image_points[0], image_points[1], (0, 0, 255), 2)
    cv2.line(image, image_points[0], image_points[2], (0, 255, 0), 2)  
    cv2.line(image, image_points[0], image_points[3], (255, 0, 0), 2) 

def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    arucoDict = cv2.aruco.Dictionary_get(aruco_dict_type)
    arucoParams = cv2.aruco.DetectorParameters_create()
    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, arucoDict, parameters=arucoParams)

    if len(corners) > 0:
        for i in range(0, len(ids)):
            
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 50, matrix_coefficients,
                                                                           distortion_coefficients)

      
            cv2.aruco.drawDetectedMarkers(frame, corners)
            # Drawing the  pose axes 
            draw_axes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec)
            translation_vector = tvec
            rotation_vector = rvec
            # Compute center of the marker
            xc = int(np.mean(corners[i][:, :, 0]))
            yc = int(np.mean(corners[i][:, :, 1]))

    return frame

def markers(s):

    img = cv2.imread(s)
    width = 1000
    h, w, _ = img.shape
    height = int(width * (h / w))
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

    intrinsic_camera = np.array(((207.66132141, 0, 251.41218615), (0, 205.751007, 338.91119239), (0, 0, 1)))
    distortion = np.array((0.07640411, -0.06229856, 0.01462332, 0.0039293, 0.00467759))

    detected_markers = pose_estimation(img, cv2.aruco.DICT_4X4_50, intrinsic_camera, distortion)
    cv2.imshow("ArUco Detected Image", detected_markers)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

markers(r"D:\CV and Drones\marker_2.jpg")