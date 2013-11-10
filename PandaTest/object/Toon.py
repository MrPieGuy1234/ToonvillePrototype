'''
Created on Nov 6, 2013

@author: Donny
'''

from actor.ActorToon import ActorToon

from Object import Object
class Toon(Object):
    def __init__(self, name="Toon"):
        Object.__init__(self, name)
        Object.setModel(self, ActorToon, True)