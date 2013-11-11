'''
Created on Nov 9, 2013

@author: Donny
'''
from utils.Utils import Log
class ZoneHandler():
    currentZone = None
    currentToon = None
    @staticmethod
    def setCurrentZone(zone):
        if ZoneHandler.currentToon is not None:
            if ZoneHandler.currentZone is not None:
                ZoneHandler.currentZone.unload()
            ZoneHandler.currentZone = zone
            zone.load(ZoneHandler.currentToon)
        else:
            Log.sendError("You must specify the current toon before loading a zone!")
    @staticmethod
    def getCurrentZone():
        return ZoneHandler.currentZone