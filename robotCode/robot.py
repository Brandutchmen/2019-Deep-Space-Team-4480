#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre
import navx
from networktables import NetworkTables

from robotpy_ext.autonomous import AutonomousModeSelector
from robotpy_ext.common_drivers import units

from components import drive, color, sensors

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):

        #NetworkTables Init
        NetworkTables.initialize()
        self.networkTable = NetworkTables.getTable("SmartDashboard")

        #PowerDistributionPanel Init
        self.pdp = wpilib.PowerDistributionPanel()

        #Motor Init
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        #SpeedControllerGroups Init
        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

        #Sensor Init
        self.ultrasonic = wpilib.AnalogInput(0)

        #Setting Drive
        self.robotDrive = wpilib.RobotDrive(self.left, self.right)

        #Controller Init
        self.playerOne = wpilib.XboxController(0)

        #Navx Init
        #self.navx = navx.AHRS.create_spi()
        self.navx = "placeholder"

        #Drive.py init
        self.drive = drive.Drive(self.robotDrive, self.navx, self.left, self.right)

        #Sensors.py init
        self.sensors = sensors.Sensors(self.robotDrive, self.navx, self.left, self.right, self.ultrasonic)

        #Color.py init
        self.color = color.PrintColor()

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        if self.sensors.closeRangeUltrasonicDetect():
            self.color.printGreen("Object Detected")
        else:
            self.color.printRed("No object")

        self.drive.masterDrive(self.playerOne.getY(0), self.playerOne.getX(0))

if __name__ == "__main__":
    wpilib.run(MyRobot)
