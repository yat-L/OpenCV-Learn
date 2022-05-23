import Converter as Con
import Sliders
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


    frameName = "Pencil Invert"
    cv.namedWindow(frameName)
    Imgfilter = Con.Converter()
    trackBar = Sliders.Sliders(frameName)
    while webCam.isOpened():
        available, frame = webCam.read()
        if available:
            #cv.imshow('frame', frame)
            #result = Imgfilter.convert(frame)
            result = trackBar.showFrame(frame)
            cv.imshow(frameName, result)

            quitKey = cv.pollKey()
            if quitKey == ord('q'):  # break when pressed 'q'
                break
            elif quitKey == ord('s'):
                cv.imwrite('screenShot.jpg',result)
                break
        else:
                break






if __name__ == "__main__":
    main()
