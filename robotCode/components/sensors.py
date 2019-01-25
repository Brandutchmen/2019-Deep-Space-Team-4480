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

class Sensors(object):

    def __init__(self, robotDrive, navx, leftMotorGroup, rightMotorGroup, closeRangeUltrasonic, outerLeftIR, leftIR, rightIR, outerRightIR):

        self.closeRangeUltrasonic = closeRangeUltrasonic
        self.outerLeftIR = outerLeftIR
        self.leftIR = leftIR
        self.rightIR = rightIR
        self.outerRightIR = outerRightIR


    def seekTape(self):

        if self.leftIR.get() and self.rightIR.get():
            return 0
            #print("Tape is on target")
        elif self.leftIR.get():
            return 1
            #print("Tape is slightly to the left of target")
        elif self.rightIR.get():
            return 2
            #print("Tape is slightly to the right of target")
        elif self.outerLeftIR.get():
            return 3
            #print("Tape is way to the left")
        elif self.outerRightIR.get():
            return 4
            #print("Tape is way to the right")
        else:
            return 5
            #print("Nothing")

    def closeRangeUltrasonicDetect(self):
        if self.closeRangeUltrasonic.getVoltage() < 4.9:
            return(True) # Object Detected
        else:
            return(False) # No Object
