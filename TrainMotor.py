# motor example from
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import os

from guizero import App, PushButton, yesno, Text, Slider, Box
if os.name == "posix":
    from gpiozero import LED
import sys
# import time
from time import sleep
from Train_classes import train

# FORWARD  =0
# BACKWARDS=1
RIGHT = 0
LEFT = 1

if os.name == "posix":
    # pin def
    Red_Led = LED(14)
    Yellow_Led = LED(15)
    Green_led = LED(18)
    button_Pin = 7  # purple

my_train = train()


def do_nothing():
    print("Doing nothing")


def do_this_on_close():
    if yesno("Close", "Do you want to quit?"):
        my_train.train_exit()
        app.destroy()
        sys.exit()


def do_start_motor():
    my_train.motor_start()
    button_message.text = "Starting motor"


def do_shut_down_motor():
    my_train.speed = 0 
    button_speed.text = my_train.speed
    my_train.motor_shut_down()
    button_message.text = "Shutting down motor"


def do_left_direction():
    my_train.set_direction(LEFT)
    button_message.text = "Going left"


def do_right_direction():
    my_train.set_direction(RIGHT)    
    button_message.text = "Going right"


def do_increase_speed():
    my_train.motor_increase_speed()
    # train_defs.menu_motor_increase_speed(my_train)
    button_speed.text = my_train.speed
    button_message.text = "Speeding up"


def do_descrease_speed():
    my_train.motor_decrease_speed()
    #train_defs.menu_motor_decrease_speed(my_train)
    button_speed.text = my_train.speed
    button_message.text = "Slowing Down"


# def do_display_speed():
#     menu_motor_decrease_speed(my_train)
#     button_speed.text = my_train.speed

      
def do_slider_speed():
    # print ("new speed is: " + str(slider_speed.value),end='')
    slider_speed.color = "red"
    # TBD change the speed directly
    my_train.motor_set_speed(slider_speed.value)


def do_exit_menu():
    button_message.text = "Exiting"
    my_train.train_exit()
    app.destroy()
    sys.exit()
    
# texts for menu. TBD: change names to meaningful


text_exit = "   EXIT    "
text_left = "Go Left"
text_right = "Go Right"
text_speed = "Speed: " + str(my_train.speed)  # YIGAL - First declaration, never used.


app = App(title="Train Control menu", bg="gray", width=500, height=700)


# TBD does not work. How to send messages to the GUI?
# text_msg.after(1000)
# I am using a button as a display, because I do not know how to write to test box


space_box0 = Box(app, width=500, height=50)
space_box0.border = False
# text_msg = Text(space_box0, text=my_train.msg_to_display)

button_message = PushButton(space_box0, command=do_nothing,
                            text="", width=50, height=5, align="left")
button_message.text_color = "blue"
button_message.text_size = 25


power_box = Box(app, width=500, height=100)
power_box.border = False
text_start = "Start Motor"
button_start = PushButton(power_box, command=do_start_motor,
                          text=text_start, height=5, align="right")
button_start.text_color = "black"
button_start.bg = "green"
button_start.text_size = 20

text_shut = "Shut Motor "
button_shut = PushButton(power_box, command=do_shut_down_motor,
                         text=text_shut, height=5, align="left")
button_shut.text_color = "black"
button_shut.bg = "red"
button_shut.text_size = 20

space_box1 = Box(app, width=500, height=20)
space_box1.border = False

direction_box = Box(app, width=500, height=100)
direction_box.border = False
button_left = PushButton(direction_box, command=do_left_direction, text=text_left, height=4, align="left")
button_right = PushButton(direction_box, command=do_right_direction, text=text_right, height=4, align="right")
button_left.text_color = "black"
button_left.bg = "#ff8000"
button_left.text_size = 20
button_right.text_color = "black"
button_right.bg = "#ff8000"
button_right.text_size = 20

space_box2 = Box(app, width=500, height=20)
space_box2.border = False

speed_box = Box(app, width=500, height=100)
speed_box.border = False

text_faster = "Faster     "
button_faster = PushButton(speed_box, command=do_increase_speed, text=text_faster, height=4, align="left")
button_faster.text_color = "yellow"
button_faster.bg = "blue"
button_faster.text_size = 20

text_slower = "Slower     "
button_slower = PushButton(speed_box, command=do_descrease_speed, text=text_slower, height=4, align="left")

button_slower.text_color = "yellow"
button_slower.bg = "blue"
button_slower.text_size = 20

text_speed = "  0  "  # YIGAL - Second declaration, deleted the first value.
button_speed = PushButton(speed_box, command=do_nothing, text=text_speed, height=4, align="right")
button_speed.text_color = "blue"
button_speed.bg = "white"
button_speed.text_size = 40
button_speed.width = 6

space_box3 = Box(app, width=500, height=20)
space_box3.border = False

slider_box = Box(app, width=500, height=100)
slider_box.border = True
slider_speed = Slider(slider_box, command=do_slider_speed, start=0, end=100, width=500, height=50)

space_box4 = Box(app, width=500, height=20)
space_box4.border = False

controls_box = Box(app, width=500, height=100)
controls_box.border = False
button_exit = PushButton(controls_box, do_exit_menu, text=text_exit)
button_exit.text_color = "black"
button_exit.bg = "yellow"
button_exit.text_size = 40

app.when_closed = do_this_on_close

app.display()
print("exiting")
app.destroy()

my_train.train_exit()
sys.exit()
