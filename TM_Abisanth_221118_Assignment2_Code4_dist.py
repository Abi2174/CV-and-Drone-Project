import cv2
import numpy as np

def undistort(s):
    
    distorted_img = cv2.imread(s)
    gray = cv2.cvtColor(distorted_img, cv2.COLOR_BGR2GRAY)
    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (6, 9), None)

    if ret:
        
        objp = np.zeros((6 * 9, 3), np.float32)
        objp[:, :2] = np.mgrid[0:6, 0:9].T.reshape(-1, 2)
        objpoints = [objp]
        imgpoints = [corners]

        # Performing camera calibration
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        # Undistort the image
        undistorted_img = cv2.undistort(distorted_img, mtx, dist)

        # Display the undistorted image
        cv2.imshow('Original Image', distorted_img)
        cv2.imshow('Undistorted Image', undistorted_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Chessboard corners not found. Unable to undistort.")
        cv2.imshow('Original Image', distorted_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


undistort(r"D:\CV and Drones\checker_board.jpeg")
