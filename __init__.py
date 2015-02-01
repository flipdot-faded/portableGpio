def create(name):
    mod = __import__(name+
    return mod.GPIO()

IN = 'in'
OUT = 'out'
