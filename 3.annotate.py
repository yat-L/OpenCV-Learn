import cv2 as cv

image = cv.imread("data/human.jpg")
cv.imshow("image", image)
cv.waitKey(0)
imageWithLine = image.copy()
pointA = (0,200)
pointB = (450,80)
cv.line(imageWithLine, pointA, pointB, (255, 0, 0), thickness=3, lineType=cv.LINE_AA)
cv.imshow('Image Line', imageWithLine)
cv.waitKey(0)
