import cv2 as cv
import Converter as Con

class Sliders:

    def __init__(self, winName):
        self.ImgFilter = Con.Converter()
        cv.createTrackbar("Sigma S", winName, 60, 100, self.changeSigma_S)
        #cv.createTrackbar("Shade", winName, 0.1, 100, self.changeSigma_S)
        #cv.createTrackbar("Sigma R", winName, 60, 100, self.changeSigma_S)
        cv.createTrackbar("Sigma X/Y", winName, 0, 5, self.changeSigma_XY)
        cv.createTrackbar("Kernel Size", winName, 5, 50, self.changeKernalSize)

    def changeSigma_S(self,val):
        self.ImgFilter.sigmaS = val

    def changeSigma_XY(self,val):
        self.ImgFilter.sigmaXY = val

    def changeKernalSize(self,val):
        size = val if val % 2 == 1 else val + 1
        self.ImgFilter.blurKer = size

    def showFrame(self,frame):
        return self.ImgFilter.convert(frame)

