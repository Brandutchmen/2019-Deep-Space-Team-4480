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

        #########################
        #####   PID LOOPS   #####
        #########################
        #turnController PID Loop
        kP = .01
        kI = 0.0001

        turnController = wpilib.PIDController(
            kP,
            kI,
            0,
            0,
            self.gyro,
            output=self.blackbox,
            )

        turnController.setInputRange(-180.0, 180.0)
        turnController.setOutputRange(-.5, .5)
        turnController.setContinuous(True)
        self.turnController = turnController
        #########################

        #########################
        #Auto Forward PID Loop
        autoForwardP = 0.006
        autoForward = wpilib.PIDController(
            autoForwardP,
            0, # I
            0, # D
            0, # F
            self.gyro,
            output=self.autoForwardOutput,
            )

        autoForward.setInputRange(-250000, 250000.0)  # I don't know what to put for the input range
        autoForward.setOutputRange(-0.5, 0.5)
        autoForward.setContinuous(False)
        autoForward.setPercentTolerance(1.5)
        self.autoForward = autoForward
        #########################

        #########################
        #Auto Turn PID Loop
        autoP = 0.006
        autoTurn = wpilib.PIDController(
            autoP,
            0,
            0.05,
            0,
            self.gyro,
            output=self.autoTurnOutput,
            )
        autoTurn.setInputRange(-180.0, 180.0)
        autoTurn.setOutputRange(-.5, .5)
        autoTurn.setContinuous(True)
        autoTurn.setPercentTolerance(0.001)
        self.autoTurn = autoTurn
        #########################

    def autoTurnOutput(self, output):
        self.autoTurnVelocity = output

    def setAutoTurn(self, angle):
        self.autoTurn.setSetpoint(angle)

    def autoForwardOutput(self, output):
        self.forwardVelocity = output

    def setAutoSetpoint(self, angle):
        self.autoForward.setSetpoint(angle)

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

        if self.turnController.isEnabled() and self.autoForward.isEnabled() and not self.autoForward.onTarget():
            self.autoTurn.disable()
            self.robotDrive.arcadeDrive(self.blackboxOutput * -1, self.forwardVelocity, False)

        elif self.autoForward.isEnabled() and not self.autoForward.onTarget():
            self.turnController.disable()
            self.autoTurn.disable()
            self.robotDrive.arcadeDrive(0, self.forwardVelocity, False)

        elif self.autoTurn.isEnabled() and not self.autoTurn.onTarget():
            self.turnController.disable()
            self.autoForward.disable()
            self.robotDrive.arcadeDrive(0, self.autoTurnVelocity * -1, False)

        else:
            self.turnController.disable()
            self.autoForward.disable()
            self.autoTurn.disable()
            self.robotDrive.tankDrive(posX, posY)
        #####################################


    def blackbox(self, output):
        self.blackboxOutput = output

    def setTurnControllerPoint(self, angle):
        self.turnController.setSetpoint(angle)

    def oneEighty(self):
        currentAngle = self.getYaw()
        if currentAngle >= 0:
            self.setTurnControllerPoint(currentAngle - 180)
        else:
            self.setTurnControllerPoint(currentAngle + 180)
        self.pidEnabled(True)

    def autoOneEighty(self):
        currentAngle = self.getYaw()
        if currentAngle >= 0:
            self.setAutoTurn(currentAngle - 180)
        else:
            self.setAutoTurn(currentAngle + 180)


    def pidEnabled(self, isEnabled):
        if isEnabled:
            self.turnController.enable()
        else:
            self.turnController.disable()
