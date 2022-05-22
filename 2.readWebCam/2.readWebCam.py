import Converter as Con
import cv2 as cv


def main():
    webCam = cv.VideoCapture(0)

    if not webCam.isOpened():
        print('Error in reading Webcam')
    else:
        fps = webCam.get(cv.CAP_PROP_FPS)
        print(f'The web cam framerate is: {fps}')
        frameCount = webCam.get(cv.CAP_PROP_FRAME_COUNT)
        print(f'Fame Count is: {frameCount}')


    convert = Con.Converter()
    while webCam.isOpened():
        available, frame = webCam.read()
        if available:
            result = convert.show(frame)
            #result = convertAndShow(frame, 60, 0.07, 0.1, 5, 0)

            quitKey = cv.pollKey()
            if quitKey == ord('q'):  # break when pressed 'q'
                break
            elif quitKey == ord('s'):
                cv.imwrite('screenShot.jpg',result)
                break
        else:
                break


def convertAndShow(frame, sigmaS, sigmaR, shade, blurKer, SigmaXY):
            frame = cv.GaussianBlur(frame, (blurKer,blurKer), SigmaXY)
            sk_gray, sk_color = cv.pencilSketch(frame, sigma_s=sigmaS, sigma_r=sigmaR, shade_factor=shade) # pencil effect
            result = cv.bitwise_not(sk_gray) # invert the color
            cv.imshow('Frame',result)
            return result



if __name__ == "__main__":
    main()
