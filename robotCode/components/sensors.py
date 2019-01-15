#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math

class Sensors(object):

    def __init__(self, robotDrive, navx, leftMotorGroup, rightMotorGroup, closeRangeUltrasonic):

        self.closeRangeUltrasonic = closeRangeUltrasonic        

    def closeRangeUltrasonicDetect(self):
        if self.closeRangeUltrasonic.getVoltage() < 4.9:
            return(True)
        else:
            return(False)
