from init import *


def rgb2hsi(rgbimg):

    rows, cols = rgbimg[:, :, 0].shape
    s = np.zeros((rows, cols), dtype=np.float32)
    i = np.zeros((rows, cols), dtype=np.float32)

    # Normalize
    red = rgbimg[:, :, 0] / 255
    green = rgbimg[:, :, 1] / 255
    blue = rgbimg[:, :, 2] / 255

    h = []

    for r in range(rows):
        for c in range(cols):
            RG = red[r, c]-green[r, c]+0.001  # Red-Green, add a constant to prevent undefined value
            RB = red[r, c]-blue[r, c]+0.001  # Red-Blue
            GB = green[r, c]-blue[r, c]+0.001  # Green-Blue
            theta = np.arccos(np.clip(((0.5*(RG+RB))/(RG**2+RB*GB)**0.5), -1, 1))  # Still in radians
            theta = np.degrees(theta)  # Convert to degrees
            if blue[r, c] <= green[r, c]:
                h.append(theta)
            else:
                h.append(360 - theta)

    h = np.array(h, dtype=np.int64).reshape(rows, cols)  # Convert Hue to NumPy array
    h = ((h - h.min()) * (1/(h.max() - h.min()) * 360))  # Scale h to 0-360
    minRGB = np.minimum(np.minimum(red, green), blue)
    s = 1-((3/(red+green+blue+0.001))*minRGB)  # Add 0.001 to prevent divide by zero
    i = (red+green+blue)/3  # Intensity: 0-1

    return h, s, i