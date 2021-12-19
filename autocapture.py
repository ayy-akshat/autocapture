import cv2
import time
import os

def takePic(path):
    f = path.split("/")[0]
    if (not os.path.exists(f)):
        os.mkdir(f)
    
    capture = cv2.VideoCapture(0)

    while True:
        picture, frame = capture.read()
        cv2.imwrite(path, frame)
        break

    capture.release()
    cv2.destroyAllWindows()

def takePictures(repeat, interval, prefix="capture", folder="captures"):
    for i in range(0, repeat):
        p = folder + "/" + prefix + str(i) + ".png"
        takePic(p)
        time.sleep(interval)

def main():
    folder = ""
    while len(folder) < 2:
        folder = input("Enter the name of the folder to store the files in (AT LEAST 2 CHARACTERS LONG): ")
    
    pre = ""
    while len(pre) < 2:
        pre = input("Enter the prefix of the captured files' names (AT LEAST 2 CHARACTERS LONG): ")
    
    repeat = 1
    r = ""
    while not (r.isnumeric() and (not '.' in r)):
        r = input("Enter how many times to take a picture (MUST BE AN INTEGER): ")
    repeat = int(r)

    interval = 1
    i = ""
    while not (i.isnumeric()):
        i = input("Enter the interval in seconds between each picture (MUST BE AN INTEGER): ")
    interval = int(i)

    takePictures(repeat, interval, pre, folder)
    print("done taking pictures. they are in the captures folder local to this file")

main()