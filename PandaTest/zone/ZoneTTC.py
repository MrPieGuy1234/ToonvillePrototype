'''
Created on Nov 9, 2013

@author: Donny
'''
from Zone import Zone
class ZoneTTC(Zone):
    def __init__(self):
        Zone.__init__(self, "models/maps/toontown_central.egg")
        self.setSpawnPoint(0, 18, 4)
        self.setSpawnRot(180)