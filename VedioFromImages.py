import cv2
import matplotlib.pyplot as plt
import RawToImage
import random

ax1 = plt.subplot(111)

def grab_frame(p):
    # test = random.randint(0, 2)
    image = cv2.imread('images/'+RawToImage.map[p])
    print(p)
    # image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image



def makeFirstFace():
    print("testafgs")
    ax1 = plt.subplot(111)
    im1 = ax1.imshow(grab_frame('SIL'))
    plt.ion()
    plt.ioff()  # due to infinite loop, this gets never called.
    plt.show()


def makeFaceAnimation(phonemeList):
    #create axes
    ax1 = plt.subplot()
    #create image plot
    im1 = ax1.imshow(grab_frame('SIL'))

    plt.ion()

    for p in phonemeList:
        # print(p)
        im1.set_data(grab_frame(p))
        plt.pause(0.1)

    im1.set_data(grab_frame('SIL'))
    plt.ioff() # due to infinite loop, this gets never called.
    plt.show()

    plt.close()
    # # print("testafgs")
    # # ax1 = plt.subplot(111)
    # im1 = ax1.imshow(grab_frame('W'))
    # plt.ion()
    # plt.ioff()  # due to infinite loop, this gets never called.
    # plt.show()


