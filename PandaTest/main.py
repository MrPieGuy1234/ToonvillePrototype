from direct.showbase.ShowBase import ShowBase
from object.Object import Object
from actor.ActorToon import ActorToon
class TestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        base.disableMouse()
        base.camera.setHpr(0,350.53,0)
        
        self.stand = Object("stand")
        self.stand.setModel("models/modelstand.egg")
        self.stand.setPosition(0, 7, -1.90)
        self.stand.setHpr(350, 0, 0)
        
        self.obj = Object("test")
        self.obj.setModel(ActorToon("neutral", False))
        self.obj.setPosition(0, 7, -1.53)
        self.obj.setHpr(255.96, 0.00, 0.00)
        self.obj.setScale(.33, .33, .33)
        
        
        
app = TestApp()
app.run()