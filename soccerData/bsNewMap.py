# coding=utf-8
import bs
import math
import random
from bsMap import *

class soccer(Map):
    import soccerDefs as defs
    name = "soccer"

    playTypes = ['melee','football','teamFlag','keepAway']

    @classmethod
    def getPreviewTextureName(cls):
        return 'footballpre'

    @classmethod
    def onPreload(cls):
        data = {}
        data['models'] = (bs.getModel('hockeyStadiumOuter'),
                                       bs.getModel('hockeyStadiumInner'),
                                       bs.getModel('hockeyStadiumStands'))
        data['vrFillModel'] = bs.getModel('footballStadiumVRFill')
        data['collideModel'] = bs.getCollideModel('hockeyStadiumCollide')
        data['tex'] = bs.getTexture('soccerMap')
        data['standsTex'] = bs.getTexture('footballStadium')

        m = bs.Material()
        m.addActions(actions=('modifyPartCollision','friction',0.01))
        data['iceMaterial'] = m
        return data
    
    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode("terrain",
                               delegate=self,
                               attrs={'model':self.preloadData['models'][0],
                                      'collideModel':self.preloadData['collideModel'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial'),self.preloadData['iceMaterial']]})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillModel'],
                          'vrOnly':True,
                          'lighting':False,
                          'background':True,
                          'colorTexture':self.preloadData['standsTex']})
        self.floor = bs.newNode("terrain",
                                attrs={"model":self.preloadData['models'][1],
                                       "colorTexture":self.preloadData['tex'],
                                       "opacity":0.92,
                                       "opacityInLowOrMediumQuality":1.0,
                                       "materials":[bs.getSharedObject('footingMaterial'),self.preloadData['iceMaterial']]})
        self.stands = bs.newNode("terrain",
                                 attrs={"model":self.preloadData['models'][2],
                                        "visibleInReflections":False,
                                        "colorTexture":self.preloadData['standsTex']})
        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.floorReflection = True
        bsGlobals.debrisFriction = 0.3
        bsGlobals.debrisKillHeight = -0.3

        bsGlobals.tint = (1.2,1.3,1.33)
        bsGlobals.ambientColor = (1.15,1.25,1.6)
        bsGlobals.vignetteOuter = (0.66,0.67,0.73)
        bsGlobals.vignetteInner = (0.93,0.93,0.95)
        bsGlobals.vrCameraOffset = (0,-3.8,-1.1)
        bsGlobals.vrNearClip = 0.5

registerMap(soccer)

