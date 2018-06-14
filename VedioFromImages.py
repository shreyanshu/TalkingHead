import cv2
import matplotlib.pyplot as plt
import RawToImage
import random

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

    #create image plot
    im1 = ax1.imshow(grab_frame('SIL'))

    plt.ion()

    for p in phonemeList:
        im1.set_data(grab_frame(p))
        plt.pause(0.5)

    im1.set_data(grab_frame('SIL'))
    plt.ioff() # due to infinite loop, this gets never called.
    plt.show()


