#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math
from components.sensors import SensorState

class Drive(object):

    def __init__(self, robotDrive, navx, leftMotorGroup, rightMotorGroup, sensors, color):

        self.left = leftMotorGroup
        self.right = rightMotorGroup

        self.robotDrive = robotDrive
        self.gyro = navx

        self.sensors = sensors
        self.color = color

    def boundHalfDegrees(self, angle_degrees):
        while angle_degrees >= 180.0:
            angle_degrees -= 360.0
        while angle_degrees < -180.0:
            angle_degrees += 360.0
        return angle_degrees

    def resetGyro(self):
        self.gyro.zeroYaw()

    def getYaw(self):
        return self.gyro.getYaw()


        #####################################
        #####   MASTER DRIVE FUNCTION   #####
        #####################################

    def masterDrive(self, posX, posY, enable=True):
        if enable == False:
            pass
        else:
            self.robotDrive.arcadeDrive(-posX, posY)
        #####################################

        #####################################
        #####    TAPE DRIVE FUNCTION    #####
        #####################################

    def tapeDrive(self, posX, posY):
        adjustmentSpeed = posY + 0.35
        majorAdjustmentSpeed = posY + 0.5

        if self.sensors.seekTape() == SensorState.OnTarget or self.sensors.seekTape() == SensorState.Nothing:
            self.masterDrive(posX, posY)
        elif self.sensors.seekTape() == SensorState.SlightLeft:
            # Tape is slightly to the left of target
            self.masterDrive(posX, posY+adjustmentSpeed)
        elif self.sensors.seekTape() == SensorState.SlightRight:
            # Tape is slightly to the right of target
            self.masterDrive(posX, posY-adjustmentSpeed)
        elif self.sensors.seekTape() == SensorState.WayLeft:
            # Tape is way to the left of target
            self.masterDrive(posX, posY+majorAdjustmentSpeed)
        elif self.sensors.seekTape() == SensorState.WayRight:
            # Tape is way to the right of target
            self.masterDrive(posX, posY-majorAdjustmentSpeed)

        '''

        #self.navx.reset()

    def autoAlign(self):
        speed = 0.5
        if self.navx.getYaw() > 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), speed)
        elif self.navx.getYaw() < 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), -speed)
        elif self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), 0)

        if self.playerOne.getAButton():
            self.autoAlign()
        elif self.playerOne.getBButton():
            self.navx.reset()
        else:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), self.playerOne.getX(0))


            '''

    def pidEnabled(self, isEnabled):
        if isEnabled:
            self.turnController.enable()
        else:
            self.turnController.disable()
