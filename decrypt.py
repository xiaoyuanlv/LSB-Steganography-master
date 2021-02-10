from LSBSteg import *

#decoding
im = cv2.imread("secret.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())