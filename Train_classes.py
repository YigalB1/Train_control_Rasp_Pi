import train_defs
import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BCM)
GPIO.setup(train_defs.in1,GPIO.OUT)
GPIO.setup(train_defs.in2,GPIO.OUT)
GPIO.setup(train_defs.en,GPIO.OUT)
GPIO.output(train_defs.in1,GPIO.LOW)
GPIO.output(train_defs.in2,GPIO.LOW)
speed=GPIO.PWM(train_defs.en,1000)

class train:
    def __init__(self):
        """
        All data should be initialized with default values or arguments sent to __init__.
        ####################################
        e.x.: def __init__(self, car_keys):
            car_keys = car_keys
        ####################################
        """
        self.car_keys = None  # TODO - do an enum of KEYS_ON and KEYS_OFF, to stop/start the car
        self.direction = None
        self.speed = None
        self.fdist = None
        self.bdist = None
        self.curr_dist = None  # the relevant dist
        self.debug_car_go = None  # used just for debug, to move info about stages
        self.debug_wifi = None

    def motor_start(self):
        """
        This function will start the engine.
        :return:
        """
        # Here will be the code for starting the engine.
        # According to your initialized data from init of car_keys.
        # it will be implemented in some way, possibly like that:
        # I think the value of ON/OFF should be encapsulated some how. The string is just an example.
        self.car_keys = "ON"

    def motor_shut_down(self):
        # The "pass" is a place holder. there are not empty fonctions in python - that is the way to implement one.
        # When adding code to the functions - the "pass" should be deleted.
        pass

    def motor_set_direction(self, _direction):
        if _direction==train_defs.FORWARD:
            GPIO.output(train_defs.in1,GPIO.HIGH)
            GPIO.output(train_defs.in2,GPIO.LOW)
        else:
            GPIO.output(train_defs.in1,GPIO.LOW)
            GPIO.output(train_defs.in2,GPIO.HIGH)

    def motor_go_faster(self):
        pass

    def motor_go_slower(self):
        pass

    # assuming direction was set already
    def motor_set_speed(_speed):
        speed.ChangeDutyCycle(_speed)
        