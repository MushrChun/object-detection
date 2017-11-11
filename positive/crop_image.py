import cv2

path = './twinings/object.jpg'

img = cv2.imread(path)
resized_img = cv2.resize(img,(50, 50))
cv2.imwrite(path, resized_img)