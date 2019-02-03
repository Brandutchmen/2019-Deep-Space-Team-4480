#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre
import hal
import rev
#import navx
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

        #Spark Max init
        self.brushless1 = rev.CANSparkMax(5, rev.MotorType.kBrushless)
        self.brushless2 = rev.CANSparkMax(6, rev.MotorType.kBrushless)

        #Intake Motor
        self.intake = ctre.WPI_TalonSRX(7)

        #Ramp Motor
        self.ramp = ctre.WPI_TalonSRX(8)

        #SpeedControllerGroups Init
        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)
        self.lift = wpilib.SpeedControllerGroup(self.brushless1, self.brushless2)

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
        #self.navx = navx.AHRS.create_spi()
        self.navx = "Placeholder"
        #Sensors.py init
        self.sensors = sensors.Sensors(self.robotDrive, self.navx, self.left, self.right, self.ultrasonic, self.outerLeftIR, self.leftIR, self.rightIR, self.outerRightIR)

        #SensorState init
        self.SensorState = sensors.SensorState()

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

        if self.playerOne.getAButton():
            self.drive.tapeDrive(self.playerOne.getY(0), self.playerOne.getX(0))
        else:
            self.drive.masterDrive(self.playerOne.getY(0), self.playerOne.getX(0), True)

        if self.playerOne.getBButton():
            self.lift.set(self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1)
        elif self.playerOne.getYButton():
            self.intake.set(self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1)
        elif self.playerOne.getXButton():
            self.ramp.set(self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1)

if __name__ == "__main__":
    wpilib.run(MyRobot)
