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
            print("Tape is on target")
            return SensorState.OnTarget
        elif not self.leftIR.get():
            print("Tape is slightly to the left of target")
            return SensorState.SlightLeft
        elif not self.rightIR.get():
            print("Tape is slightly to the right of target")
            return SensorState.SlightRight
        elif not self.outerLeftIR.get():
            print("Tape is way to the left")
            return SensorState.WayLeft
        elif not self.outerRightIR.get():
            print("Tape is way to the right")
            return SensorState.WayRight
        else:
            print("Nothing")
            return SensorState.Nothing

    def closeRangeUltrasonicDetect(self):
        if self.closeRangeUltrasonic.getVoltage() < 4.9:
            return(True) # Object Detected
        else:
            return(False) # No Object
