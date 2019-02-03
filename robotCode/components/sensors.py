#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math

'''
SENSOR LAYOUT

IR sensors are to be placed ~ 3-4 inches from the ground on the outer parts of the robot frame

SENSOR KEY:
    0. Outer Left IR
    1. Left IR
    2. Right IR
    3. Outer Right IR

  - - - - - -
|0          3|

|   1    2   |

|            |
  - - - - - -

'''
class SensorState(object):
    OnTarget, SlightLeft, SlightRight, WayLeft, WayRight, Nothing = range(0, 6)

class Sensors(object):

    def __init__(self, robotDrive, navx, leftMotorGroup, rightMotorGroup, closeRangeUltrasonic, outerLeftIR, leftIR, rightIR, outerRightIR):

        self.closeRangeUltrasonic = closeRangeUltrasonic
        self.outerLeftIR = outerLeftIR
        self.leftIR = leftIR
        self.rightIR = rightIR
        self.outerRightIR = outerRightIR


    def seekTape(self):

        if self.leftIR.get() == False and self.rightIR.get() == False:
            return SensorState.OnTarget
        elif not self.leftIR.get():
            return SensorState.SlightLeft
        elif not self.rightIR.get():
            return SensorState.SlightRight
        elif not self.outerLeftIR.get():
            return SensorState.WayLeft
        elif not self.outerRightIR.get():
            return SensorState.WayRight
        else:
            return SensorState.Nothing

    def closeRangeUltrasonicDetect(self):
        if self.closeRangeUltrasonic.getVoltage() < 4.9:
            return(True) # Object Detected
        else:
            return(False) # No Object
