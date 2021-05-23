import cv2
import numpy as np

#starting the video
video = cv2.VideoCapture(0)

#reading the image behind the black screen
image = cv2.imread("Buddha Statue.jpg")

#loop
while (video.isOpened()):
    #reading every frame of the video
    ret, frame = video.read()

    #resizing the image and video frame
    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640, 480))

    #darker and lighter shades of black
    upper_black = np.array([104, 153, 70])
    lower_black = np.array([30, 30, 0])

    #mask
    mask = cv2.inRange(frame, lower_black, upper_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    #real video
    f = frame - res
    #returning image when black color is found
    f = np.where(f == 0, image, f)

    #real video + mask
    output = cv2.addWeighted(f, 1, image, 0, 0)

    #window name
    cv2.imshow("background", output)
    #wating for a key to be pressed
    key = cv2.waitKey(1)

    #unicode character for escape key
    if key & 0xFF == 27:
        break
    #checking if q is pressed
    if key & 0xFF == ord('q'):
        break

#closing the window and cam
video.release()
cv2.destroyAllWindows()