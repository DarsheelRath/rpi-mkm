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