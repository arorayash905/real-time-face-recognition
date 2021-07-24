import test
import cv2

img = cv2.imread('try.jpeg')
image = test.fun(img)
cv2.imwrite("Recognized5.jpg", image)
print("Image is Saved.")
cv2.imshow("Image", image)
cv2.waitKey(0)
