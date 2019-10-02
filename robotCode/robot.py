#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre
import hal
import rev
from networktables import NetworkTables
from wpilib.shuffleboard import Shuffleboard
from robotpy_ext.autonomous import AutonomousModeSelector
from robotpy_ext.common_drivers import units
from components import drive, color, sensors, intake

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        #Watchdog
        #self.watchdog = wpilib.Watchdog
        #self.watchdog.enable(self)

        #Onboard Webcam Init
        wpilib.CameraServer.launch()

        #NetworkTables Init
        NetworkTables.initialize()
        self.networkTable = NetworkTables.getTable("SmartDashboard")

        #PowerDistributionPanel Init
        self.pdp = wpilib.PowerDistributionPanel()

        #Drive Motor Init
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        #Spark Max Init
        if not wpilib.RobotBase.isSimulation():
            self.brushless1 = rev.CANSparkMax(5, rev.MotorType.kBrushless)
            self.brushless2 = rev.CANSparkMax(6, rev.MotorType.kBrushless)
        else:
           self.brushless1 = ctre.WPI_TalonSRX(5)
           self.brushless2 = ctre.WPI_TalonSRX(6)


        #Intake Motor Init
        self.intakeMotors = ctre.WPI_TalonSRX(7)

        #Ramp Motor Init
        self.ramp = ctre.WPI_TalonSRX(8)

        #SpeedControllerGroups Init
        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)
        self.lift = wpilib.SpeedControllerGroup(self.brushless1, self.brushless2)

        #Ir Init
        self.intakeSensor = wpilib.DigitalInput(9)
        self.outerLeftIR = wpilib.DigitalInput(0)
        self.leftIR = wpilib.DigitalInput(1)
        self.rightIR = wpilib.DigitalInput(2)
        self.outerRightIR = wpilib.DigitalInput(3)

        #Setting Drive
        self.robotDrive = wpilib.drive.DifferentialDrive(self.left, self.right)

        #Controller Init
        self.playerOne = wpilib.XboxController(0)

        #Navx Init
        #self.navx = navx.AHRS.create_spi()
        self.navx = "Placeholder"

        #Sensors.py Init
        self.sensors = sensors.Sensors(self.robotDrive, self.navx, self.left, self.right, self.outerLeftIR, self.leftIR, self.rightIR, self.outerRightIR)

        #SensorState Init
        self.SensorState = sensors.SensorState()

        #Color.py Init
        self.color = color.PrintColor()

        #Drive.py Init
        self.drive = drive.Drive(self.robotDrive, self.navx, self.left, self.right, self.sensors, self.color)

        #Intake.py Init
        self.intake = intake.Intake(self.robotDrive, self.playerOne, self.intakeMotors, self.lift, self.intakeSensor)

        '''
        # Add the elevator motor and potentiometer to an 'Elevator' tab
        elevatorTab = Shuffleboard.getTab("Elevator")
        elevatorTab.add(title="Motor", value=0.4)
        elevatorTab.add(title="Potentiometer", value=0.3)
        '''

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

        '''
        if self.playerOne.getAButton():
            self.lift.set(0.17322)
        else:
            self.lift.set((self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1)*0.3)


        if self.playerOne.getBButton():
            self.drive.tapeDrive(-self.playerOne.getX(0), self.playerOne.getY(0))
        else:
        '''

        if self.playerOne.getAButton():
            self.intake.intakeIn(0, (self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1)*0.3)
        else:
            self.lift.set(self.playerOne.getY(1)*-0.3)
            self.intakeMotors.set((self.playerOne.getTriggerAxis(1) + self.playerOne.getTriggerAxis(0) * -1))

        if self.playerOne.getXButton():
            self.ramp.set(1)
        elif self.playerOne.getYButton():
            self.ramp.set(-1)
        else:
            self.ramp.set(0)



        self.drive.masterDrive(self.playerOne.getX(0), -self.playerOne.getY(0))

if __name__ == "__main__":
    wpilib.run(MyRobot)
