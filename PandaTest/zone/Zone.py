'''
Created on Nov 5, 2013

@author: Donny
'''
from utils.Utils import Loader, Log
from object.Object import Object

import collections
class Zone:
    map = None
    modelList = None
    isLoaded = False
    def __init__(self, mapModel):
        self.map = Loader.loadModel(mapModel)
    def addObjectsOnLoad(self, objects):
        if isinstance(objects, collections.Iterable):
            self.modelList.extend(objects)
        else:
            self.modelList.append(objects)
    def load(self):
        self.map.reparentTo(render)
        try:
            for x in len(self.modelList):
                self.modelList[x].reparentTo(self.map)
        except TypeError:
            Log.sendWarning("No objects to load on map")
        self.isLoaded = True
    def unload(self):
        try:
            for x in len(self.modelList):
                self.modelList[x].remove()
        except TypeError:
            Log.sendWarning("No objects to remove")
        self.map.remove()
        self.isLoaded = False
    def setMap(self, mapModel):
        if self.isLoaded:
            self.map = Loader.loadModel(mapModel)