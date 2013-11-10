'''
Created on Nov 9, 2013

@author: Donny
'''
import sys
class Loader():
    @staticmethod
    def loadModel(modelPath):
        try:
            model = loader.loadModel(modelPath)
        except IOError:
            model = loader.loadModel("models/err.egg")
            Log.sendWarning("Could not load model: " + modelPath)
        return model

class Log():
    @staticmethod
    def sendError(err):
        print("!!ERROR!! " + err)
        sys.exit(1)
    @staticmethod
    def sendWarning(err):
        print("!!WARNING!! " + err)
    