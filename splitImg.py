import cv2
import os

def run_main():
    for x in range(0,6):
        file_name = f'page{x}.jpg'
        print (file_name)

        splitImsge(file_name)


def splitImsge(file_name):
    #file_name = 'page0.jpg'
    basename = os.path.basename(file_name).split('.')[0]

    img = cv2.imread(file_name)

    [h,w] = img.shape[:2]
    print (f"the h is {h} , the w is {w}")

    upperSkip = 290
    lowSkip = 170
    imgH = h - upperSkip - lowSkip
    upperPath = basename + '_01.jpg'
    middlePath = basename + '_02.jpg'
    lowPath = basename + '_03.jpg'
    #upperPath = basename + '_upper2.jpg'
    #middlePath = basename + '_middle2.jpg'
    #lowPath = basename + '_low2.jpg'

    upper1 = upperSkip
    upper2 = upperSkip + int(imgH/3)

    middle1 = upperSkip + int(imgH/3)
    middle2 = upperSkip + int(imgH/3)*2

    low1 = upperSkip + int(imgH/3)*2
    low2 = upperSkip + int(imgH)
    
    #upperImg = img[:int(h/3),:,:]
    #middleImg = img[int(h/3):int(h/3)*2,:,:]
    #lowImg = img[int(h/3)*2:,:,:]
    upperImg = img[upper1:upper2,:,:]
    middleImg = img[middle1:middle2,:,:]
    lowImg = img[low1:low2,:,:]
    
    cv2.imwrite(upperPath, upperImg)
    cv2.imwrite(middlePath, middleImg)
    cv2.imwrite(lowPath, lowImg)

if __name__ == "__main__":
    run_main()
