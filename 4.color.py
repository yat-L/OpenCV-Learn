import cv2 as cv

rubik = cv.imread("data/rubiks.jpg")
rubikLAB = cv.cvtColor(rubik,cv.COLOR_BGR2LAB)
(L,A,B) = cv.split(rubikLAB)
cv.imshow('frame1',L)
cv.imshow('frame2',A)
cv.imshow('frame3',B)
cv.waitKey(0)
