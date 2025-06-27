def LED():
    print('Looking for an LED on GPIO17, Configure this file for a diffrent GPIO pin')
    from gpiozero import LED as rpipinLED
    import time
    while True:
        led = rpipinLED(17)
        led.on()
        time.sleep(2)
        led.off()
        time.sleep(2)
def mcpi():
    print('Looking for a Minecraft Pi server on port 4711')
    from mcpi import minecraft
    from time import sleep
    print('Waiting one minute for Minecraft Pi to start')
    mc = minecraft.Minecraft.create()
    mc.postToChat("Hello Minecraft World!")
    mc.postToChat("Start Building!")
    while True:
        pass
def OpenCV_test():
    print('Configure this file for a diffrent image, and download a picture with realistic faces with the name "opencv-facedetect.jpg, and change the letter x to your python version"')
    import cv2

    cv2data = '/usr/local/lib/pythonx/dist-packages/cv2/data'
    facecascade = (cv2data +  'haarcascade_frontalface_default.xml')
    img = cv2.data.imread('opencv-facedetect.jpg')
    scale_factor = 1.4
    min_neighbours = 5

    faces = face_cascade.detectMultiScale(img, scale_factor, min_neighbours)
    print(faces)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
