import cv2

def main():
    webCam = cv2.VideoCapture(0)

    if not webCam.isOpened():
        print('Error in reading Webcam')
    else:
        fps = webCam.get(cv2.CAP_PROP_FPS)
        print(f'The web cam framerate is: {fps}')
        frameCount = webCam.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f'Fame Count is: {frameCount}')

    while webCam.isOpened():
        available, frame = webCam.read()
        if available:
            sk_gray, sk_color = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.1) # pencil effect
            result = cv2.bitwise_not(sk_gray) # invert the color
            cv2.imshow('Frame',result)
            quitKey = cv2.waitKey(1)
            if quitKey == ord('q'):  # break when pressed 'q'
                break
        else:
                break




if __name__ == "__main__":
    main()
