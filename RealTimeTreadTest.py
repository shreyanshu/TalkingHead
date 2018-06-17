import cv2
import matplotlib.pyplot as plt
import RawToImage
import random
import threading
import time

def grab_frame(p):
    # test = random.randint(0, 2)
    image = cv2.imread('images/'+RawToImage.map[p])
    print(p)
    # image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

ax1 = plt.subplot(111)
im1 = ax1.imshow(grab_frame('SIL'))
# plt.ion()
# plt.pause(0.9)


def makeStartFace():
    im1 = ax1.imshow(grab_frame('AA'))
    plt.ion()
    plt.pause(.9)


def makeFaceAnimation():
    im1.set_data(grab_frame('AA'))
    plt.pause(.9)
    im1.set_data(grab_frame('W'))
    plt.ioff()  # due to infinite loop, this gets never called.
    plt.show()


thread1 = threading.Thread(target=makeFaceAnimation)
thread1.start()
thread1.join()
thread2 = threading.Thread(target=makeFaceAnimation)
# thread2.join()
thread2.start()
# makeFirstFace()
# time.sleep(.5)
# makeFaceAnimation()

