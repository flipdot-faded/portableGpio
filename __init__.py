def create(name):
    gpioClass = __import__(name+'.GPIO')
    return gpioClass()

IN = 'in'
OUT = 'out'
