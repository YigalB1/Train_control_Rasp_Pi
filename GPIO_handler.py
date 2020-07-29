import os

if os.name == "posix":
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


def initialize():
    if os.name == "posix":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)


def shut_down():
    if os.name == "posix":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)


def cleanup():
    if os.name == "posix":
        GPIO.cleanup()


def get_speed_control():
    if os.name == "posix":
        return speed_control


def set_right():
    if os.name == "posix":
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)


def set_left():
    if os.name == "posix":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
