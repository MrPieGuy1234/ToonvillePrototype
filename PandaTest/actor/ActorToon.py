'''
Created on Nov 8, 2013

@author: Donny
'''

from direct.actor.Actor import Actor
from utils.Utils import Log
class ActorToon(Actor):
    def __init__(self, defaultAnimation, hasShoes):
        try:
            Actor.__init__(self, 
            {"head":"models/tt_a_chr_dgm_shorts_head_1000.bam",
             "torso":"models/tt_a_chr_dgm_shorts_torso_1000.bam",
             "legs":"models/tt_a_chr_dgm_shorts_legs_1000.bam"},
            {"head":{"neutral":"models/anim/toonHead/tt_a_chr_dgm_shorts_head_neutral.bam",
                     "run":"models/anim/toonHead/tt_a_chr_dgm_shorts_head_run.bam",
                     "runjump":"models/anim/toonHead/tt_a_chr_dgm_shorts_head_leap_zhang.bam",
                     "walk":"models/anim/toonHead/tt_a_chr_dgm_shorts_head_walk.bam",
                     "jump":"models/anim/toonHead/tt_a_chr_dgm_shorts_head_jump-zhang.bam"},
             "torso":{"neutral":"models/anim/toonTorso/tt_a_chr_dgm_shorts_torso_neutral.bam",
                      "run":"models/anim/toonTorso/tt_a_chr_dgm_shorts_torso_run.bam",
                      "runjump":"models/anim/toonTorso/tt_a_chr_dgm_shorts_torso_leap_zhang.bam",
                      "walk":"models/anim/toonTorso/tt_a_chr_dgm_shorts_torso_walk.bam",
                      "jump":"models/anim/toonTorso/tt_a_chr_dgm_shorts_torso_jump-zhang.bam"},
             "legs":{"neutral":"models/anim/toonLegs/tt_a_chr_dgm_shorts_legs_neutral.bam",
                     "run":"models/anim/toonLegs/tt_a_chr_dgm_shorts_legs_run.bam",
                     "runjump":"models/anim/toonLegs/tt_a_chr_dgm_shorts_legs_leap_zhang.bam",
                     "walk":"models/anim/toonLegs/tt_a_chr_dgm_shorts_legs_walk.bam",
                     "jump":"models/anim/toonLegs/tt_a_chr_dgm_shorts_legs_jump-zhang.bam"}})
            self.loop(defaultAnimation)
            self.attach("head", "torso", "def_head")
            self.attach("torso", "legs", "joint_hips")
        except IOError:
            Log.sendError("err")
            Actor.__init__(self, 'models/err.egg')
        if hasShoes is False:
            self.find("**/shoes").hide()
            self.find("**/boots_short").hide()
            self.find("**/boots_long").hide()

        