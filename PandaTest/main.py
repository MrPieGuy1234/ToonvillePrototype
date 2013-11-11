from direct.showbase.ShowBase import ShowBase
from actor.ActorToon import ActorToon
from object.Object import Object
from object.Toon import Toon
from zone.ZoneHandler import ZoneHandler
from zone.ZoneTTC import ZoneTTC
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        base.disableMouse()
        
        self.toon = Toon()
        self.toon.setColor(1, 0, 0)
        
        ZoneHandler.currentToon = self.toon
        ZoneHandler.setCurrentZone(ZoneTTC())
        ZoneHandler.getCurrentZone().map.ls()
        
        base.camera.reparentTo(self.toon.parent)
        base.camera.setPos(0,-20,7.25)
        base.camera.setP(352.5)
        
app = TestApp()
app.run()