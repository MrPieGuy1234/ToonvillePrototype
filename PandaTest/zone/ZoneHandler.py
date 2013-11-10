'''
Created on Nov 9, 2013

@author: Donny
'''

class ZoneHandler():
    currentZone = None
    @staticmethod
    def setCurrentZone(zone):
        if ZoneHandler.currentZone is not None:
            ZoneHandler.currentZone.unload()
        ZoneHandler.currentZone = zone
        zone.load()
    @staticmethod
    def getCurrentZone():
        return ZoneHandler.currentZone