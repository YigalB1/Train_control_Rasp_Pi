# motor eample from
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

# from gui example
from guizero import App,PushButton,yesno,Text,Slider,Box
from gpiozero import LED
import sys
import time

# from regular example
# import RPi.GPIO as GPIO          
from time import sleep

# import train classes
import train_defs
from Train_classes import train

#FORWARD  =0
#BACKWARDS=1
RIGHT = 0
LEFT  = 1

# pin def
Red_Led = LED(14)
Yellow_Led = LED(15)
Green_led = LED(18)
button_Pin = 7 # purple  

#in1 = 24
#in2 = 23
#en = 25

temp1=1

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(train_defs.in1,GPIO.OUT)
#GPIO.setup(train_defs.in2,GPIO.OUT)
#GPIO.setup(train_defs.en,GPIO.OUT)
#GPIO.output(train_defs.in1,GPIO.LOW)
#GPIO.output(train_defs.in2,GPIO.LOW)
#speed=GPIO.PWM(train_defs.en,1000)


my_train = train()


#my_train.motor_start()
#print (my_train.speed)


def do_nothing ():
    print ("Nothing happened")

def do_this_on_close():
    print("exiting from do_this_on_close 0")
    if yesno("Close", "Do you want to quit?"):
        print("exiting from do_this_on_close 1")
        GPIO.cleanup()
        app.destroy()
        print("exiting from do_this_on_close2")
        sys.exit()
        
        


 
def do_start_motor():
    my_train.motor_start()
    
def do_shut_down_motor():
    my_train.motor_shut_down()

def do_left_direction():
    my_train.set_direction(LEFT)

def do_right_direction():
    my_train.set_direction(RIGHT)




def do_increase_speed():
    my_train.motor_increase_speed()
    #train_defs.menu_motor_increase_speed(my_train)
    button5.text = my_train.speed
    
def do_descrease_speed():
    my_train.motor_decrease_speed()
    #train_defs.menu_motor_decrease_speed(my_train)
    button5.text = my_train.speed
    
def do_display_speed():
    train_defs.menu_motor_decrease_speed(my_train)
    button5.text = my_train.speed

      
def do_slider_speed():
    #print ("new speed is: " + str(slider_speed.value))
    slider_speed.color="red"
    # TBD change the speed directly

def do_exit_menu():
    my_train.train_exit()
    app.destroy()
    sys.exit()
    



# texts for menu. TBD: change names to meaningful
text3="Faster     "
text4="Slower     "
text5="  0  "
text_exit ="   EXIT    "
text_left = "Go Left"
text_right = "Go Right"
text_speed = "Speed: " + str(my_train.speed)
print(text_speed)


app = App(title="Train Control menu", bg = "gray",width=500, height=600)


power_box = Box(app, width=500, height=100)
power_box.border = False
button1 = PushButton(power_box, command=do_start_motor,     text="Start Motor",height=5,align="right")
button1.text_color="black"
button1.bg="green"
button1.text_size=20
button2 = PushButton(power_box, command=do_shut_down_motor, text="Shut Motor ", height=5,align="left")
button2.text_color="black"
button2.bg="red"
button2.text_size=20

space_box1 = Box(app, width=500, height=20)
space_box1.border = False



direction_box = Box(app, width=500, height=100)
direction_box.border = False
button_left = PushButton(direction_box, command=do_left_direction, text=text_left, height=4,align="left")
button_right = PushButton(direction_box, command=do_right_direction, text=text_right,height=4,align="right")
button_left.text_color="black"
button_left.bg="#ff8000"
button_left.text_size=20
button_right.text_color="black"
button_right.bg="#ff8000"
button_right.text_size=20


space_box2 = Box(app, width=500, height=20)
space_box2.border = False



speed_box = Box(app, width=500, height=100)
speed_box.border = False
button3 = PushButton(speed_box, command=do_increase_speed, text=text3, height=4,align="left")
button4 = PushButton(speed_box, command=do_descrease_speed, text=text4,height=4,align="left")
button5 = PushButton(speed_box, command=do_display_speed, text=text5,height=4,align="right")
button3.text_color="yellow"
button3.bg="blue"
button3.text_size=20
button4.text_color="yellow"
button4.bg="blue"
button4.text_size=20
button5.text_color="blue"
button5.bg="white"
button5.text_size=40
button5.width=6

space_box3 = Box(app, width=500, height=20)
space_box3.border = False

slider_box = Box(app, width=500, height=100)
slider_box.border = True
slider_speed = Slider(slider_box,command=do_slider_speed,start=0,end=100,width=500,height=50)

space_box4 = Box(app, width=500, height=20)
space_box4.border = False

controls_box = Box(app, width=500, height=100)
controls_box.border = False
button_exit = PushButton(controls_box, do_exit_menu, text=text_exit)
button_exit.text_color="black"
button_exit.bg="yellow"
button_exit.text_size=40

app.when_closed = do_this_on_close

app.display()
print("exiting")
app.destroy()

GPIO.cleanup()
sys.exit()





#speed.start(25)
#print (train_defs.FORWARD)
while True:
    my_train.motor_set_direction(train_defs.FORWARD)
    my_train.motor_set_speed(15)
    time.sleep(3)
    print(".",end='')
    my_train.motor_set_speed(15)
    time.sleep(3)
    print(".",end='')
    my_train.motor_set_direction(train_defs.BACKWARDS)
    my_train.motor_set_speed(100)
    time.sleep(3)
    print("^",end='')
    my_train.motor_set_speed(100)
    time.sleep(3)
    print("^",end='')







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
        #speed.ChangeDutyCycle(25)
        my_train.motor_set_speed(25)
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
        #GPIO.cleanup()
        my_train.train_exit()
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