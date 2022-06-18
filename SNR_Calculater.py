from init import *


def calculate_snr_ycbcr(original, converted):
    ibg = 0
    signal = ((original + converted) / 2 - ibg).sum()
    f = (0.5 ** 0.5) * ((2 / pi) ** -0.5)
    noise = np.abs(original - converted).sum() * f
    snr = signal / noise
    return print(f"RGB to YCBCR Img SNR value is {snr} dB")


def calculate_snr_hsi(original, converted):
    ibg = 0
    signal = ((original + converted) / 2 - ibg).sum()
    f = (0.5 ** 0.5) * ((2 / np.pi) ** -0.5)
    noise = np.abs(original - converted).sum() * f
    snr = signal / noise
    return print(f"RGB to HSI Img SNR value is {snr} dB")