#import library
import cv2

#get the image location and file name
img_location = 'C:/Users/User/Pictures/Saved Pictures/'
file_name = 'elon-musk.jpg'

#read in the image
img = cv2.imread(img_location + file_name)

#convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert the image
inverted_gray_image = 255 - gray_image

#blur the image by gaussain function
blur_image = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

#invert the blurred image
invert_blurred_image = 255 - blur_image

#create the pencil sketch img
pencil_sketch_img = cv2.divide(gray_image, invert_blurred_image,scale=256.0)

#show the image
cv2.imshow('Original image',img)
cv2.imshow('New image',pencil_sketch_img)
cv2.waitKey(0)