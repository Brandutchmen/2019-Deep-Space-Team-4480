#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib
import math

class Drive(object):

    def __init__(self, robotDrive, navx, leftMotorGroup, rightMotorGroup):

        self.left = leftMotorGroup
        self.right = rightMotorGroup

        self.robotDrive = robotDrive
        self.gyro = navx

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

    def masterDrive(self, posX, posY):

            self.robotDrive.arcadeDrive(-posX, posY)
        #####################################
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
