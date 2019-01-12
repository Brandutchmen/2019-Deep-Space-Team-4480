#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre
import navx
from networktables import NetworkTables

from robotpy_ext.autonomous import AutonomousModeSelector
from robotpy_ext.common_drivers import units

from components import drive

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):

        #NetworkTables Init
        NetworkTables.initialize()
        self.networkTable = NetworkTables.getTable("SmartDashboard")

        #PowerDistributionPanel INIT
        self.pdp = wpilib.PowerDistributionPanel()

        #Motor Init
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        #Sensor Init
        self.ultrasonic = wpilib.AnalogInput(0)
        self.distanceSensor = navx.AHRS.create_i2c()

        #Controller Init
        self.playerOne = wpilib.XboxController(0)

        #Navx Init
        self.navx = navx.AHRS.create_spi()

        #Setting Drive
        self.robotDrive = wpilib.RobotDrive(self.motor1, self.motor2, self.motor3, self.motor4)

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        #self.navx.reset()
        #This is a note
        pass

    def teleopPeriodic(self):
        if self.ultrasonic.getVoltage() < 4.9:
            print("Close Range - Object Detected")
        else:
            print("No Object")

        if self.playerOne.getAButton():
            self.autoAlign()
        elif self.playerOne.getBButton():
            self.navx.reset()
        else:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), self.playerOne.getX(0))

    def autoAlign(self):
        speed = 0.5
        if self.navx.getYaw() > 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), speed)
        elif self.navx.getYaw() < 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), -speed)
        elif self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), 0)

if __name__ == "__main__":
    wpilib.run(MyRobot)
