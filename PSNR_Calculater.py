from init import *


def calculate_psnr(original, converted):
    original = original.astype(np.float32) / 255.
    converted = converted.astype(np.float32) / 255.
    mse = np.mean((original - converted) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def rgb2hsi_psnr(img, HSI_img):
    original = img
    converted = HSI_img
    value = calculate_psnr(original, converted)
    print(f"RGB to HSI Img PSNR value is {value} dB")


def rgb2ycrcb_psnr(img, YCrCb_img):
    original = img
    converted = YCrCb_img
    value = calculate_psnr(original, converted)
    print(f"RGB to YCrCb Img PSNR value is {value} dB")