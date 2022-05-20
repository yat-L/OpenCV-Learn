import cv2
import os

def main():
    dataDir = os.path.dirname("data/")
    humanImg = os.path.join(dataDir, "human.jpg")
    print(humanImg)

    img_grayscale = cv2.imread(humanImg,cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(humanImg,cv2.IMREAD_COLOR)
    img_unchanged = cv2.imread(humanImg,cv2.IMREAD_UNCHANGED)
    cv2.imshow('grayscale',img_grayscale)
    cv2.imshow('color',img_color)
    cv2.imshow('unchanged',img_unchanged)
    cv2.waitKey(0)

    cv2.imwrite(os.path.join(dataDir,'human-grayscale.jpg'),img_grayscale)
    cv2.imwrite(os.path.join(dataDir,'human-color.jpg'),img_color)
    cv2.imwrite(os.path.join(dataDir,'human-unchanged.jpg'),img_unchanged)

if __name__ == "__main__":
    main()
