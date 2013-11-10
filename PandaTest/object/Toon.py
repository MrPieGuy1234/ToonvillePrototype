'''
Created on Nov 6, 2013

@author: Donny
'''

from actor.ActorToon import ActorToon

from Object import Object
class Toon(Object):
    def __init__(self, name="Toon"):
        Object.__init__(self, name)
        self.setModel(ActorToon("neutral", False))
    def setColor(self, r, g, b):
        self.model.find("**/feet").setColor(r,g,b)
        self.model.find("**/legs").setColor(r,g,b)
        self.model.find("**/arms").setColor(r,g,b)
        self.model.find("**/neck").setColor(r,g,b)
        self.model.find("**/head").setColor(r,g,b)
        self.model.find("**/head-front").setColor(r,g,b)