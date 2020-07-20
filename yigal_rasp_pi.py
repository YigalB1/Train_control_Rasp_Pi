
# motor example from
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

from guizero import App,PushButton,yesno,Text,Slider,Box
from gpiozero import LED
import sys
# import time
from time import sleep
from Train_classes import train
import tkinter


#FORWARD  =0
#BACKWARDS=1
RIGHT = 0
LEFT  = 1

# pin def
#Red_Led = LED(14)
#Yellow_Led = LED(15)
#Green_led = LED(18)
#button_Pin = 7 # purple  

my_train = train()


def do_nothing ():
    print ("Doing nothig")

def do_this_on_close():
    if yesno("Close", "Do you want to quit?"):
        my_train.train_exit()
        app.destroy()
        sys.exit()
 
def do_start_motor():
    my_train.motor_start()
    button_message.text="Starting motor"
    
def do_shut_down_motor():
    my_train.speed = 0 
    button_speed.text = my_train.speed
    my_train.motor_shut_down()
    button_message.text="Shutting down motor"

def do_left_direction():
    my_train.set_direction(LEFT)
    button_message.text="Going left"

def do_right_direction():
    my_train.set_direction(RIGHT)    
    button_message.text="Going right"

def do_increase_speed():
    my_train.motor_increase_speed()
    #train_defs.menu_motor_increase_speed(my_train)
    button_speed.text = my_train.speed
    button_message.text="Speeding up"
    
def do_descrease_speed():
    my_train.motor_decrease_speed()
    #train_defs.menu_motor_decrease_speed(my_train)
    button_speed.text = my_train.speed
    button_message.text="Slowing Down"
    
def do_display_speed():
    menu_motor_decrease_speed(my_train)
    button_speed.text = my_train.speed

      
def do_slider_speed():
    #print ("new speed is: " + str(slider_speed.value),end='')
    slider_speed.color="red"
    # TBD change the speed directly
    my_train.motor_set_speed(slider_speed.value)

def do_exit_menu():
    button_message.text="Exiting"
    my_train.train_exit()
    app.destroy()
    sys.exit()
   


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
import PyQt5.QtWidgets as Qw
from PyQt5.QtWidgets import *

class ControlTrainPannel(QWidget):

    def __init__(self, app):
        super().__init__()
        self.title = 'Train Control Pannel'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.App = app

        self.initUI(App)
    
    def initUI(self, App):
        btn_minHeight = 80
        btn_minWidth = 80   # Currently have no impact
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.App.setStyle('Fusion')
        palette = QPalette()
        self.App.setPalette(palette)
        self.setStyleSheet("background-color: gray;")

        layout = QVBoxLayout()
        
        button_start = QPushButton('Start Motor', self)
        button_start.setToolTip('Press button to start')
        button_start.clicked.connect(do_start_motor)
        button_start.setStyleSheet('color: black; background-color: green; font-size: 20pt; font-family: Courier;')
        button_start.setMinimumSize(btn_minWidth, btn_minHeight)


        button_shut = QPushButton("Shut Motor", self)
        button_shut.setToolTip('Press button to stop the engine')
        button_shut.clicked.connect(do_shut_down_motor)
        button_shut.setStyleSheet('color: black; background-color: red; font-size: 20pt; font-family: Courier;')
        button_shut.setMinimumSize(btn_minWidth, btn_minHeight)





        button_left = QPushButton("Left", self)
        button_left.setToolTip('Press button change direction to the left')
        button_left.clicked.connect(do_left_direction)
        button_left.setStyleSheet('color: black; background-color: #ff8000; font-size: 20pt; font-family: Courier;')
        button_left.setMinimumSize(btn_minWidth, btn_minHeight)

        button_right = QPushButton("Right", self)
        button_right.setToolTip('Press button change direction to the right')
        button_right.clicked.connect(do_right_direction)
        button_right.setStyleSheet('color: black; background-color: #ff8000; font-size: 20pt; font-family: Courier;')
        button_right.setMinimumSize(btn_minWidth, btn_minHeight)


        speed = QSlider(Qt.Horizontal, self)
        #slider.setFocusPolicy(Qt.StrongFocus)
        speed.setTickPosition(QSlider.TicksBothSides)
        speed.setToolTip('Move to change speed')
        speed.setTickInterval(10)
        speed.setSingleStep(2)
        speed.valueChanged[int].connect(self.speed_changeValue)
        speed.setStyleSheet('color: black; background-color: blue; font-size: 20pt; font-family: Courier;')
        #speed.setMinimumSize(btn_minWidth, btn_minHeight)

        grid = Qw.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(button_start, 1, 1)
        grid.addWidget(button_shut, 1, 2)
        grid.addWidget(button_left, 2, 1)
        grid.addWidget(button_right, 2, 2)
        grid.addWidget(speed, 3, 1)
        self.setLayout(grid)
        
        self.show()


    def speed_changeValue(self):
        None
    
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

app = QApplication(sys.argv)
ex = ControlTrainPannel(app)
sys.exit(app.exec_())
GPIO.cleanup()

