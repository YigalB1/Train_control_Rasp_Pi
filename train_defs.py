FORWARD  =0
BACKWARDS=1

in1 = 24
in2 = 23
en = 25

def motor_move(speed):
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    my_train.motor_set_speed(25)
    
def motor_stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    my_train.motor_shut_down()
    
    