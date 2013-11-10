from direct.showbase.ShowBase import ShowBase
from actor.ActorToon import ActorToon
from object.Object import Object
from object.Toon import Toon
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        base.disableMouse()
        base.camera.setHpr(0,350.53,0)
        
        self.stand = Object("stand")
        self.stand.setModel("models/modelstand.egg")
        self.stand.setPosition(0, 7, -1.90)
        self.stand.setHpr(350, 0, 0)
        
        self.toon = Toon("toon")
        self.toon.setPosition(0, 7, -1.53)
        self.toon.setHpr(255.96, 0.00, 0.00)
        self.toon.setScale(.33, .33, .33)
        self.toon.setColor(1,0,0)
        
        
app = TestApp()
app.run()