import RPi.GPIO as GPIO

RIGHT = 0
LEFT  = 1

# HW pins  connecting to the L298N motor driver,
# that drives the train tracks with voltage
# in & in2 set the direction
# en is PWM signal, setting the
in1 = 24  # blue wire
in2 = 23  # brown wire
en = 25  # gray wire

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
speed_control = GPIO.PWM(en,1000)

'''
# check if GPIO channels are active
# if yes: clean them
# 0 means Output
# 1 means Input

func=GPIO.gpio_function(in1)
print (func)
print (GPIO.gpio_function(in1))
print (GPIO.gpio_function(in2))
print (GPIO.gpio_function(en))

if (func==0):
    GPIO.cleanup(in1)
    GPIO.cleanup(in2)
    GPIO.cleanup(en)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
'''




class train:
    def __init__(self):
        self.min_speed = 0
        self.max_speed = 100
        self.speed_delta = 5
        self.speed = 0  # int between  to 100
        self.train_enginecar_keys = None  # TODO - do an enum of KEYS_ON and KEYS_OFF, to stop/start the car
        self.direction = RIGHT  # left or right
        self.keys_on = False
        self.msg_to_display = ""
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

    def motor_start(self):
        # GPIO.clenup()
        self.speed=0
        speed_control.start(0)
        self.msg_to_display="starting Engine"
        self.keys_on=True
        self.set_direction(self.direction) # keep the last direction

    def motor_shut_down(self):
        if self.keys_on == True:
            self.keys_on = False
            self.speed = 0
            speed_control.stop()            
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)

    def set_direction(self, _direction):
        # TBD - add check if direction is changing.
        # if yes: wait 2 seconds to avoid damage to engine
        if self.keys_on == False:
            return

        if _direction == RIGHT:
            self.direction = RIGHT
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            # print(">>>",end='')
        else:
            self.direction = LEFT
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            # print("<<<",end='')

    def motor_increase_speed(self):
        if self.keys_on == False:
            return
        self.speed += self.speed_delta

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        speed_control.ChangeDutyCycle(self.speed)

    def motor_decrease_speed(self):
        if self.keys_on == False:
            return

        self.speed -= self.speed_delta
        if self.speed < self.min_speed:
            self.speed = self.min_speed
        speed_control.ChangeDutyCycle(self.speed)
    
    def train_exit(self):
        self.keys_on = False
        speed_control.stop()
        GPIO.cleanup()
    
    # assuming direction was set already
    def motor_set_speed(self,_speed):
        if self.keys_on==False:
            return

        self.speed = _speed
        speed_control.ChangeDutyCycle(self.speed)
