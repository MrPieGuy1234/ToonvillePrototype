'''
Created on Nov 5, 2013

@author: Donny
'''
from utils.Utils import Loader
from object.Object import Object
import collections
class Zone:
    map = None
    modelList = None
    def __init__(self, mapModel):
        Zone.map = Loader.loadModel(mapModel)
    def addObjectsOnLoad(self, objects):
        if isinstance(objects, collections.Iterable):
            self.modelList.extend(objects)
        else:
            self.modelList.append(objects)
    def load(self):
        pass
    def unload(self):
        pass
    