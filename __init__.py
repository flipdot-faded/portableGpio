import imp
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

def create(name):
    mod = imp.load_source(name, cur_dir+'/'+name+'.py')
    return mod.GPIO()

IN = 'in'
OUT = 'out'
