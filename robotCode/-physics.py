
from pyfrc.physics import drivetrains
from pyfrc.physics.units import units
from pyfrc.physics import tankmodel, motors

'''

I am having some pyfrc.physics motors import issues. Until I resolve them, this document will be unused

'''


class PhysicsEngine(object):

    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''

        self.physics_controller = physics_controller

        self.drivetrain = tankmodel.TankModel.theory(motors.MOTOR_CFG_CIM_IMP,
                                                     robot_mass=90 * units.lbs,
                                                     gearing=10.71, nmotors=2,
                                                     x_wheelbase=2.0*feet,
                                                     wheel_diameter=6*units.inch)
#        self.physics_controller.add_device_gyro_channel('navxmxp_spi_4_angle')

    def update_sim(self, hal_data, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated.

            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''

        # Simulate the drivetrain
        lr_motor = hal_data['CAN'][1]['value']
        rr_motor = hal_data['CAN'][2]['value']
        lf_motor = hal_data['CAN'][3]['value']
        rf_motor = hal_data['CAN'][4]['value']

        # TODO: get motor values from hal_data
        velocity, rotation = self.drivetrain.get_vector(l_motor, r_motor)

#        speed = 5

#        speed, rotation = drivetrains.FourMotorDrivetrain(lr_motor, rr_motor, lf_motor, rf_motor, speed=speed)
        self.physics_controller.drive(velocity, rotation, tm_diff)
