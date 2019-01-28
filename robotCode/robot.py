#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre
import hal
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
        self.outerLeftIR = wpilib.DigitalInput(0)
        self.leftIR = wpilib.DigitalInput(1)
        self.rightIR = wpilib.DigitalInput(2)
        self.outerRightIR = wpilib.DigitalInput(3)

        #Setting Drive
        self.robotDrive = wpilib.RobotDrive(self.left, self.right)

        #Controller Init
        self.playerOne = wpilib.XboxController(0)

        #Navx Init
        self.navx = navx.AHRS.create_spi()

        #Sensors.py init
        self.sensors = sensors.Sensors(self.robotDrive, self.navx, self.left, self.right, self.ultrasonic, self.outerLeftIR, self.leftIR, self.rightIR, self.outerRightIR)

        #Color.py init
        self.color = color.PrintColor()

        #Drive.py init
        self.drive = drive.Drive(self.robotDrive, self.navx, self.left, self.right, self.sensors, self.color)

    def disabledInit(self):
        self.networkTable.putString('status', "Disabled")

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.networkTable.putString('status', "Autonomous")

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.networkTable.putString('status', "Teleop")
        print(self.navx.getYaw())
        if self.playerOne.getAButton():
            self.drive.tapeDrive(self.playerOne.getY(0), self.playerOne.getX(0))
        else:
            self.drive.masterDrive(self.playerOne.getY(0), self.playerOne.getX(0), True)

if __name__ == "__main__":
    wpilib.run(MyRobot)
