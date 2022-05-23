
import cv2 as cv

class Converter(object):
    def __init__(self):
        self._shade = 0.1
        self._sigmaS = 60
        self._sigmaR = 0.07
        self._blurKer = 5
        self._sigmaXY = 0

    @property
    def shade(self):
        return self._shade

    @property
    def sigmaS(self):
        return self._sigmaS

    @property
    def sigmaR(self):
        return self._sigmaR

    @property
    def blurKer(self):
        return self._blurKer

    @property
    def sigmaXY(self):
        return self._sigmaXY

    @shade.setter
    def shade(self,value):
        self._shade = value

    @sigmaS.setter
    def sigmaS(self,value):
        self._sigmaS = value

    @sigmaR.setter
    def sigmaR(self,value):
        self._sigmaR = value

    @blurKer.setter
    def blurKer(self,value):
        self._blurKer = value

    @sigmaXY.setter
    def sigmaXY(self,value):
        self._sigmaXY = value


    def convert(self,frame): 
            temp = cv.GaussianBlur(frame, (self._blurKer,self._blurKer), self._sigmaXY)
            sk_gray, sk_color = cv.pencilSketch(temp, sigma_s=self._sigmaS, sigma_r=self._sigmaR, shade_factor=self._shade) # pencil effect
            result = cv.bitwise_not(sk_gray) # invert the color
            return result
