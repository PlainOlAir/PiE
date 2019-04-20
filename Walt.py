#Team 6
#Middle College High School

LF_motor = "56687019174689847830972"
LB_motor = "56699099423971639337912"
RF_motor = "56702640167271161404160"
RB_motor = "56692477276697421313848"
top_motor = "56688344425072198851691"
bottom_motor = "56691343941204961768197"

def setliftmotor(speed):
    Robot.set_value(top_motor, "duty_cycle", speed)
    Robot.set_value(bottom_motor, "duty_cycle", speed)

def setleftmotor(speed):
    Robot.set_value(LF_motor, "duty_cycle", speed)
    Robot.set_value(LB_motor, "duty_cycle", speed)
    
def setrightmotor(speed):
    Robot.set_value(RF_motor, "duty_cycle", speed)
    Robot.set_value(RB_motor, "duty_cycle", speed)

def stop():
    Robot.set_value(RF_motor, "duty_cycle", 0)
    Robot.set_value(RB_motor, "duty_cycle", 0)
    Robot.set_value(LF_motor, "duty_cycle", 0)
    Robot.set_value(LB_motor, "duty_cycle", 0)
    
def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(temp)

def autonomous_main():
    pass

async def main_left():
    setliftmotor(0.1)
    
    await Actions.sleep(1.0)
    Robot.set_value(right_motor, "duty_cycle", 0.45)
    Robot.set_value(left_motor, "duty_cycle", -0.5)
    await Actions.sleep(7.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    Robot.set_value(left_motor, "duty_cycle", -0.2)
    Robot.set_value(top_motor, "duty_cycle", 0)
    Robot.set_value(bottom_motor, "duty_cycle", 0)
    await Actions.sleep(1)
    stop()

async def main_right():
    Robot.set_value(top_motor, "duty_cycle", 0.1)
    Robot.set_value(bottom_motor, "duty_cycle", 0.1)
    await Actions.sleep(1.0)
    Robot.set_value(right_motor, "duty_cycle", 0.45)
    Robot.set_value(left_motor, "duty_cycle", -0.5)

#async def alt_left():

#async def alt_right():

async def temp():
    setleftmotor(1)
    setrightmotor(-1)
    setliftmotor(0.3)
    await Actions.sleep(4)
    setliftmotor(0)
    await Actions.sleep(3)
    stop()
    await Actions.sleep(2)
    setliftmotor(-0.3)

def teleop_setup():
    print("yes its running")

def teleop_main():
        
    joystick_x = Gamepad.get_value("joystick_left_x")
    joystick_y = Gamepad.get_value("joystick_left_y")
    V = (100-abs(joystick_x)) * (joystick_y/100) + joystick_y
    W = (100-abs(joystick_y)) * (joystick_x/100) + joystick_x
    R = (V+W)/2
    L = (V-W)/2
    
    if(R > 0.9):
        R = 0.9
    if(R < -0.9):
        R = -0.9
    if(L > 0.9):
        L = 0.9
    if(L < -0.9):
        L = -0.9
    
    if(abs(Gamepad.get_value("joystick_left_y")) > 0.1 or abs(Gamepad.get_value("joystick_left_x")) > 0.1):
        setrightmotor(R)
        setleftmotor(-1*L)
    else:
        stop()

    if(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("r_trigger") == 1):
        setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.7)
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("l_trigger") == 1):
        setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.2)
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("l_bumper") == 1):
        setliftmotor(-1*Gamepad.get_value("joystick_right_y"))
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1):
        setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.3)
    else:
        setliftmotor(1)
    