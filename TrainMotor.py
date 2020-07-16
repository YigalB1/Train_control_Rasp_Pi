# motor eample from
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

# from gui example
from guizero import App,PushButton
from gpiozero import LED
import sys

# from regular example
import RPi.GPIO as GPIO          
from time import sleep

# import train classes
import train_defs
from Train_classes import train

# pin def
Red_Led = LED(14)
Yellow_Led = LED(15)
Green_led = LED(18)
button_Pin = 7 # purple  

in1 = 24
in2 = 23
en = 25

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
speed=GPIO.PWM(en,1000)


my_train = train()

#speed.start(25)
my_train.motor_set_direction(FORWARD)
my_train.motor_set_speed(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")   




while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        speed.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        speed.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        speed.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        print("exiting")
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

print("here at 1")
sys.exit(0)


# starting the GUI part

def exitApp():
    sys.exit()
    
def toggleLED():
    Red_Led.toggle()
    if Red_Led.is_lit:
        ledButton.text = "LED OFF"
    else:
        ledButton.text = "LED ON "
        
my_app = App('First GUI', height=600,width=800)

ledButton=PushButton(my_app,toggleLED,text="LED_ON",align="top",width=15,height=3)
ledButton.text_size=36

exitButton=PushButton(my_app,exitApp,text="Exit",align="bottom",width=15,height=3)
exitButton.text_size=36

my_app.display()
print("exiting")
sys.exit()

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(Red_Led_Pin, GPIO.OUT)
GPIO.setup(Yellow_Led_Pin, GPIO.OUT)
GPIO.setup(Green_pwm_Pin, GPIO.OUT)
GPIO.setup(button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(Green_pwm_Pin,200)


# drive pins to off
GPIO.output(Red_Led_Pin, GPIO.LOW)
GPIO.output(Yellow_Led_Pin, GPIO.LOW)
pwm.start(duty_cycle)

try:

    while 1:
        print(".",end='')
        if GPIO.input(button_Pin):
            pwm.ChangeDutyCycle(duty_cycle)
            GPIO.output(Red_Led_Pin, GPIO.LOW)
            GPIO.output(Yellow_Led_Pin, GPIO.LOW)
        else:
            print("X",end='')
            pwm.ChangeDutyCycle(duty_cycle)
            GPIO.output(Red_Led_Pin, GPIO.HIGH)
            GPIO.output(Yellow_Led_Pin, GPIO.HIGH)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(100-duty_cycle)
            GPIO.output(Red_Led_Pin, GPIO.LOW)
            GPIO.output(Yellow_Led_Pin, GPIO.LOW)
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping")
    pwm.stop()
    GPIO.cleanup()