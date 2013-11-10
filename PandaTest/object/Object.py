'''
Created on Nov 5, 2013

@author: Donny
'''
from direct.actor.Actor import Actor
from utils.Utils import Loader, Log
class Object:
    containsActor = False
    x = 0
    y = 0
    z = 0
    def __init__(self, objName):
        self.parent = render.attachNewNode(objName)
    def setModel(self, model):
        if type(model) is str:
            self.model = Loader.loadModel(model)
            Object.containsActor = False
        elif isinstance(model, Actor):
            self.model = model
            Object.containsActor = True
        else:
            Log.sendError("Argument must be String or Actor")
        self.model.reparentTo(self.parent)
    def setPosition(self, x, y, z):
        self.parent.setPos(x,y,z)
    def setHpr(self, h, p, r):
        self.parent.setHpr(h,p,r)
    def setScale(self,x,y,z):
        self.parent.setScale(x,y,z)
    def setParent(self, parent):
        self.parent.reparentTo(parent)