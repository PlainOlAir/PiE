right_motor = "56699099423971639337912"
left_motor = "56690116315779879524089"
top_motor = "56693567227486137575505"
bottom_motor = "56697390661107800622028"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    Robot.set_value(top_motor, "duty_cycle", 0.1)
    Robot.set_value(bottom_motor, "duty_cycle", 0.1)
    await Actions.sleep(1.0)
    Robot.set_value(right_motor, "duty_cycle", 0.45)
    Robot.set_value(left_motor, "duty_cycle", -0.5)
    await Actions.sleep(7.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    Robot.set_value(left_motor, "duty_cycle", -0.2)
    Robot.set_value(top_motor, "duty_cycle", 0)
    Robot.set_value(bottom_motor, "duty_cycle", 0)
    await Actions.sleep(1)
    Robot.set_value(right_motor, "duty_cycle", 0)
    Robot.set_value(left_motor, "duty_cycle", 0)

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    
    joystick_x = Gamepad.get_value("joystick_left_x")
    joystick_y = -1*Gamepad.get_value("joystick_left_y")
    V = (100-abs(joystick_x)) * (joystick_y/100) + joystick_y
    W = (100-abs(joystick_y)) * (joystick_x/100) + joystick_x
    R = (V+W)/2
    L = (V-W)/2
    print("thomas is a retard")
    
    if(abs(Gamepad.get_value("joystick_left_y")) > 0.1 or abs(Gamepad.get_value("joystick_left_x")) > 0.1):
        Robot.set_value(right_motor, "duty_cycle", R)
        Robot.set_value(left_motor, "duty_cycle", -1*L)
    else:
        Robot.set_value(right_motor, "duty_cycle", 0)
        Robot.set_value(left_motor, "duty_cycle", 0)

    if(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("r_trigger") == 1):
        Robot.set_value(top_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.7)
        Robot.set_value(bottom_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.7)
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("l_trigger") == 1):
        Robot.set_value(top_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.15)
        Robot.set_value(bottom_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.15)
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1 and Gamepad.get_value("l_bumper") == 1):
        Robot.set_value(top_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y"))
        Robot.set_value(bottom_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y"))
    elif(abs(Gamepad.get_value("joystick_right_y")) > 0.1):
        Robot.set_value(top_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.3)
        Robot.set_value(bottom_motor, "duty_cycle", -1*Gamepad.get_value("joystick_right_y")*0.3)
    else:
        Robot.set_value(top_motor, "duty_cycle", 0)
        Robot.set_value(bottom_motor, "duty_cycle", 0)

    '''if abs(Gamepad.get_value("joystick_right_y")) > 0.1:
        Robot.set_value(right_motor, "duty_cycle", Gamepad.get_value("joystick_right_y"))
    else:
        Robot.set_value(right_motor, "duty_cycle", 0)
    if abs(Gamepad.get_value("joystick_left_y")) > 0.1:
        Robot.set_value(left_motor, "duty_cycle", -1*Gamepad.get_value("joystick_left_y"))
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
    if Gamepad.get.value("button_y") == 1:
        Robot.set_value(top_motor, "duty_cycle", 1)
        Robot.set_value(bottom_motor, "duty_cycle", 1)
    elif Gamepad.get.value("button_a") == 1:
        Robot.set_value(top_motor, "duty_cycle", -1)
        Robot.set_value(bottom_motor, "duty_cycle", -1)
    else:
        Robot.set_value(top_motor, "duty_cycle", 0)
        Robot.set_value(bottom_motor, "duty_cycle", 0)'''
    
    