from LSBSteg import *

#encoding
steg = LSBSteg(cv2.imread("background.jpg"))
img_encoded = steg.encode_text("Welcome to Steganography")
cv2.imwrite("secret.png", img_encoded)