import cv2
import matplotlib.pyplot as plt
import RawToImage
import GetWavFileDuration
import RawToWav
# import random
import threading
import PlayRawAudio

ax1 = plt.subplot(111)

def grab_frame(p, mouth):
    # test = random.randint(0, 2)
    image = cv2.imread('image1/'+str(mouth)+"/"+RawToImage.map[p])
    print(p)
    # image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image


def makeFirstFace():
    print("testafgs")
    ax1 = plt.subplot(111)
    # im1 = ax1.imshow(grab_frame('SIL', mouth))
    plt.ion()
    plt.ioff()  # due to infinite loop, this gets never called.
    plt.show()


def makeFaceAnimation(phonemeList, mouth):
    #create axes
    ax1 = plt.subplot()
    #create image plot
    print(mouth)
    im1 = ax1.imshow(grab_frame('SIL', mouth))
    plt.pause(0.75)
    RawToWav.run('rawFile/raw_file.raw')
    length = GetWavFileDuration.get_length('wavFile/test.wav')
    pauseTime = length/len(phonemeList)
    th = threading.Thread(target=PlayRawAudio.run)
    th.start()

    # print(pauseTime)
    # plt.pause(2)
    plt.ion()
    for p in phonemeList:
        # print(p)
        im1.set_data(grab_frame(p, mouth))
        plt.pause(pauseTime/1.2)

    im1.set_data(grab_frame('SIL', mouth))
    plt.pause(0.75)
    plt.ioff() # due to infinite loop, this gets never called.
    # plt.show()

    plt.close('all')
    return
    # # print("testafgs")
    # # ax1 = plt.subplot(111)
    # im1 = ax1.imshow(grab_frame('W'))
    # plt.ion()
    # plt.ioff()  # due to infinite loop, this gets never called.
    # plt.show()


