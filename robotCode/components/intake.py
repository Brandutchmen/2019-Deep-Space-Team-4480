#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math
from components.sensors import SensorState

class Intake(object):

    def __init__(self, robotDrive, playerOne, intakeMotors, lift, intakeSensor):
        self.robotDrive = robotDrive
        self.playerOne = playerOne
        self.intakeMotors = intakeMotors
        self.lift = lift
        self.intakeSensor = intakeSensor

    def getIntakeSensor(self):
        return self.intakeSensor.get()

    def intakeIn(self, accel, liftVar):

        if self.intakeSensor.get() == True:
            self.lift.set(-0.23 + liftVar)
            self.intakeMotors.set(0.5 + accel)
        elif self.intakeSensor.get() == False:
            self.lift.set(0)
            self.intakeMotors.set(0)
