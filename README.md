A portable gpio library. Contains abstraction for mulitple GPIO libraries.

---

Example (flip a pin):

    import portableGpio

    gpio = portableGpio.create('RaspPi') # creates abstraction for GPIO.RPi
    gpio.init()

    pin0 = gpio.create_pin(0, portableGpio.IN)
    state = pin0.get()
    print state

Reference
=========

portableGpio::create(name : string) : GPIO
---
creates a abstraction for the given libray

portableGpio::IN : GpioDirection
---
Constant for GPIO state in

portableGpio::OUT : GpioDirection
---
Constant for GPIO state out

GPIO.init()
---
Initializes the GPIO library. Please note that this does initialization using the default paramters. Each library can define another overload of init to for example set the pin layout.


GPIO.create_pin(pin : int, direction : GpioDirection) : GpioPin
---
Creates a gpio pin object (digital mode, no PWM)


GpioPin.get() : bool
---
Returns True if the pin is high otherwise False


GpioPin.set(state : bool)
---
Sets the gpio pin state to the given state
