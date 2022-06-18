from init import *

def rgb2ycbcr(im):
    xform = np.array([[0.257, 0.504, 0.098],
                      [-0.148, -0.291, 0.439],
                      [0.439, -0.368, -0.071]])
    ycbcr = im.dot(xform.T)
    ycbcr[:, :, [0]] += 16
    ycbcr[:, :, [1, 2]] += 128
    return np.uint8(ycbcr)