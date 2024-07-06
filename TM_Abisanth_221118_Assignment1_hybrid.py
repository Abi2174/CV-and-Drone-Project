import cv2
import numpy as np

def Fourier_Transform(img):
    
   
    FT_img = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    magnitude_spectrum = cv2.magnitude(FT_img[:, :, 0], FT_img[:, :, 1])
# Log-transform the magnitude spectrum for better visualization
    magnitude_spectrum_log = np.log1p(magnitude_spectrum)
# Normalize the log-transformed magnitude spectrum for display
    magnitude_spectrum_normalized = cv2.normalize(magnitude_spectrum_log, None, 0, 255, cv2.NORM_MINMAX)
    return  magnitude_spectrum_normalized


image1 = cv2.imread(r"D:\CV and Drones\kalam.jpeg")
image2 = cv2.imread(r"D:\CV and Drones\nambi.jpg")
grayscale_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayscale_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image1 = cv2.resize(grayscale_image1, (256, 256))
gray_image2 = cv2.resize(grayscale_image2, (256, 256))

# Finding Fourier Transform of Initial Images
FT_image1 = Fourier_Transform(gray_image1)
FT_image2 = Fourier_Transform(gray_image2)

# Low-pass filter
filter_size = (10, 10)
low_pass_kernel = np.ones(filter_size, np.float32) / (filter_size[0] * filter_size[1])
low_pass_filtered_image1 = cv2.filter2D(gray_image1, -1, low_pass_kernel)
low_pass_filtered_image2 = cv2.filter2D(gray_image2, -1, low_pass_kernel)

# High-pass filter (complement of low-pass filter)
high_pass_kernel = np.ones(filter_size, np.float32) - low_pass_kernel
high_pass_filtered_image2 = gray_image2 - low_pass_filtered_image2

# Resize filters to the size of the images
low_pass_kernel_resized = cv2.resize(low_pass_kernel, (256, 256))
high_pass_kernel_resized = cv2.resize(high_pass_kernel, (256, 256))

# Finding Fourier Transform of Filtered Images
FT_filtered_image1 = Fourier_Transform(low_pass_filtered_image1)
FT_filtered_image2 = Fourier_Transform(high_pass_filtered_image2)

hybrid=(low_pass_filtered_image1+high_pass_filtered_image2)/2

cv2.imshow('Filter', low_pass_kernel_resized.astype(np.uint8))
cv2.imshow('FT Img 1', FT_image1.astype(np.uint8))
cv2.imshow('FT Img 2', FT_image2.astype(np.uint8))
cv2.imshow('FT Filtered Img 1', FT_filtered_image1.astype(np.uint8))
cv2.imshow('FT Filtered Img 2', FT_filtered_image2.astype(np.uint8))
cv2.imshow('Modified Img 1',low_pass_filtered_image1.astype(np.uint8))
cv2.imshow('Modified Img 2', high_pass_filtered_image2.astype(np.uint8))
cv2.imshow('Hybrid Image', hybrid.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
