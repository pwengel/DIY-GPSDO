#from machine import Pin, Timer
#led = Pin(25, Pin.OUT)
#timer = Timer()


#def blink(timer):
#    led.toggle()
#    print("Hi")


#timer.init(period=1000, mode=Timer.PERIODIC, callback=blink)


from machine import I2C
import time
from machine import Pin

scl = Pin(21, Pin.PULL_UP)
sda = Pin(20, Pin.PULL_UP)

i2c = I2C(id=0, freq=400000, sda=sda, scl=scl)                              # create I2C peripheral at frequency of 400kHz
                                                    # depending on the port, extra parameters may be required
                                                    # to select the peripheral and/or pins to use

i2c.scan()                                          # scan for peripherals, returning a list of 7-bit addresses

while True:

    print(i2c.scan())
    print("Hi")
    i2c.writeto(76, b'\x10\x7F\xFF')                   # write 3 bytes to peripheral with 7-bit address 42
    time.sleep(1)
#i2c.readfrom(42, 4)                     # read 4 bytes from peripheral with 7-bit address 42

#i2c.readfrom_mem(42, 8, 3)     # read 3 bytes from memory of peripheral 42,
                                                    #   starting at memory-address 8 in the peripheral
#i2c.writeto_mem(42, 2, b'\x10')  # write 1 byte to memory of peripheral 42
                                                    #   starting at address 2 in the peripheral