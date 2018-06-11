import cv2
import matplotlib.pyplot as plt
import random

def grab_frame():
    test = random.randint(0, 2)
    image = cv2.imread('images/'+str(test)+'.jpg')
    print(test)
    # image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

#create axes
ax1 = plt.subplot(111)

#create image plot
im1 = ax1.imshow(grab_frame())

plt.ion()

while True:
    im1.set_data(grab_frame())
    plt.pause(0.2)

plt.ioff() # due to infinite loop, this gets never called.
plt.show()