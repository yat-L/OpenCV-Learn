import cv2 as cv
import numpy as np

rubik = cv.imread("data/rubiks.jpg")
rubikLAB = cv.cvtColor(rubik,cv.COLOR_BGR2LAB)
(L,A,B) = cv.split(rubikLAB)
L_H = A_H = B_H = None
L_H = cv.resize(L,(0,0),None,0.35,0.35)
A_H = cv.resize(A,(0,0),None,0.35,0.35)
B_H = cv.resize(B,(0,0),None,0.35,0.35)

numpyHstack = np.vstack((L_H,A_H,B_H))

cv.imshow('LAB Color',numpyHstack)
cv.waitKey(0)
