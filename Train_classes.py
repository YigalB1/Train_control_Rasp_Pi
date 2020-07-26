import GPIO_handler

RIGHT = 0
LEFT  = 1


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
        GPIO_handler.initialize()
        self.speed_control = GPIO_handler.get_speed_control()

    def motor_start(self):
        # GPIO.clenup()
        self.speed = 0
        self.speed_control.start(0)
        self.msg_to_display = "starting Engine"
        self.keys_on = True
        self.set_direction(self.direction) # keep the last direction

    def motor_shut_down(self):
        if self.keys_on == True:
            self.keys_on = False
            self.speed = 0
            self.speed_control.stop()
            GPIO_handler.shut_down()

    def set_direction(self, _direction):
        # TBD - add check if direction is changing.
        # if yes: wait 2 seconds to avoid damage to engine
        if self.keys_on == False:
            return

        if _direction == RIGHT:
            self.direction = RIGHT
            GPIO_handler.set_right()
            # print(">>>",end='')
        else:
            self.direction = LEFT
            GPIO_handler.set_left()
            # print("<<<",end='')

    def motor_increase_speed(self):
        if self.keys_on == False:
            return
        self.speed += self.speed_delta

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        self.speed_control.ChangeDutyCycle(self.speed)

    def motor_decrease_speed(self):
        if self.keys_on == False:
            return

        self.speed -= self.speed_delta
        if self.speed < self.min_speed:
            self.speed = self.min_speed
        self.speed_control.ChangeDutyCycle(self.speed)
    
    def train_exit(self):
        self.keys_on = False
        self.speed_control.stop()
        GPIO_handler.cleanup()

    # assuming direction was set already
    def motor_set_speed(self,_speed):
        if self.keys_on == False:
            return

        self.speed = _speed
        self.speed_control.ChangeDutyCycle(self.speed)
