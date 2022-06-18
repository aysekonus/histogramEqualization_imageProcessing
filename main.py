from init import *

# READING IMG
img = "images/mandrill.ppm"
RGB_Img = cv2.cvtColor(cv2.imread(img, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB) # default olarak BGR olarak gelen input görüntüsünü RGB'a dönüştürerek aldık.

# CONVERTING RGB TO HSI
h, s, i = rgb2hsi(RGB_Img)

HSI_Img = np.zeros((RGB_Img.shape[0], RGB_Img.shape[1], 3)) # Construct hsi images
HSI_Img[:, :, 0] = h
HSI_Img[:, :, 1] = s
HSI_Img[:, :, 2] = i

# CONVERTING RGB TO YCbCr
YCbCr_Img = rgb2ycbcr(RGB_Img)

# CALCULATE PSNR VALUES
rgb2hsi_psnr(RGB_Img, HSI_Img)
rgb2ycrcb_psnr(RGB_Img, YCbCr_Img)

# CALCULATE SNR VALUES
calculate_snr_hsi(RGB_Img, HSI_Img)
calculate_snr_ycbcr(RGB_Img, YCbCr_Img)

# DISPLAY OUTPUTS
cv2.imshow('Original RGB Image', RGB_Img)
cv2.imshow('RGB to HSI Image', HSI_Img)
cv2.imshow('RGB to YCbCr Image', YCbCr_Img)
cv2.waitKey(0)





