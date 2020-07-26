import RPi.GPIO as GPIO


# HW pins  connecting to the L298N motor driver,
# that drives the train tracks with voltage
# in & in2 set the direction
# en is PWM signal, setting the
in1 = 24  # blue wire
in2 = 23  # brown wire
en = 25  # gray wire

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
speed_control = GPIO.PWM(en, 1000)

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


def initialize():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)


def shut_down():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)


def cleanup():
    GPIO.cleanup()


def get_speed_control():
    return speed_control


def set_right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)


def set_left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
