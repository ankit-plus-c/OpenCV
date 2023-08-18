import cv2

## load an image using imread
img = cv2.imread("1coffee.jpg")

## print the shape of the loaded image
print(img.shape)

## resizing the image
img = cv2.resize(img,(640,480))

img = cv2.resize(img,(0,0),fx=0.1,fy=0.1)

## displaying the image
cv2.imshow("coffee",img)
cv2.waitKey(0)