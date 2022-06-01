import cv2 as cv
import numpy as np

def main():
    rubik = cv.imread("data/rubiks.jpg")
    rubikLAB = cv.cvtColor(rubik,cv.COLOR_BGR2LAB)
    rubikYCrCb = cv.cvtColor(rubik, cv.COLOR_BGR2YCrCb)
    rubikHSV = cv.cvtColor(rubik, cv.COLOR_BGR2HSV)
    display(cv.split(rubikLAB))
    display(cv.split(rubikYCrCb))
    display(cv.split(rubikHSV))


def display(tupleChannel):
    (A,B,C) = tupleChannel

    A_H = B_H = B_H = None
    A_H = cv.resize(A,(0,0),None,0.35,0.35)
    B_H = cv.resize(B,(0,0),None,0.35,0.35)
    C_H = cv.resize(C,(0,0),None,0.35,0.35)

    numpyHstack = np.vstack((A_H,B_H,C_H))
    cv.imshow('3 channel',numpyHstack)
    cv.waitKey(0)

if __name__ == "__main__":
    main()
