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
    spawnX = 0
    spawnY = 0
    spawnZ = 0
    spawnRot = 0
    def __init__(self, mapModel):
        self.map = Loader.loadModel(mapModel)
    def addObjectsOnLoad(self, objects):
        if isinstance(objects, collections.Iterable):
            self.modelList.extend(objects)
        else:
            self.modelList.append(objects)
    def load(self, currentToon):
        self.map.reparentTo(render)
        currentToon.setPosition(self.spawnX, self.spawnY, self.spawnZ)
        currentToon.setHpr(self.spawnRot, 0, 0)
        try:
            for x in len(self.modelList):
                self.modelList[x].reparentTo(self.map)
        except TypeError:
            Log.sendWarning("No objects to load on map")
        self.isLoaded = True
        
    def unload(self, currentToon):
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
    def setSpawnPoint(self, x, y, z):
        self.spawnX = x
        self.spawnY = y
        self.spawnZ = z
    def setSpawnRot(self, rot):
        self.spawnRot = rot
        