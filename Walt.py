#Team 6
#Middle College High School

#sorting algorithm for most_common
def selection_sort(lis):
    #go through all list elements        
    for i in range(len(lis)):
        minimum = i
        #finding next minimum element in unsorted list
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[minimum]:
                minimum = j
        
        #moves minimum in place of i
        lis[minimum], lis[i] = lis[i], lis[minimum]
    return lis

#apply certain functions 5 times on a number
def tennis_ball(num):
    #run tennis ball 5 times on num
    for i in range(5):
        #if number is divisible by 3, divide by 3
        if(num%3 == 0):
            num = num/3
            
        #if number is not divisible 3 and odd, 
        #mulitply by 4 and add 2
        elif(num%2 == 1 and num%3 != 0):
            num = (num*4)+2
        
        #otherwise add 1
        else:
            num = num+1
    return(int(num))  

#remove duplicate digits in a number
def remove_duplicates(num):
    #convert num into a str as it is iterable
    a = str(num)
    b = list(a)
    c = []
    final = 0

    #If the a single digit is not in list c, put it in. If it
    #is, do nothing
    #this makes a list that has the first appearance of any
    #digit in the input number
    for e in b:
        if e not in c:
            c.append(e)

    #make a number from the list of the removed duplicates
    for f in c:
        final = final * 10
        final = final + int(f)
    
    return final

#move the last digit to the beginning
def rotate(num):
    a = str(num)
    b = list(a)
    c = 0
    d = len(a)
    e = ""
    final = 0
  
    #find largest digit to loop function that amount of times
    for f in b:
        if int(f) > c:
            c = int(f)

    #loops rotate the amount of times the largest digit of the number is
    #take out the last digit and insert it in the beginning
    while(c > 0):
        c = c - 1
        e = b.pop(d-1)
        b.insert(0, e)

    #reconstruct the number
    for g in b:
        final = final * 10
        final = final + int(g)

    return final

#returns the next highest number in the Fibonacci sequence
#returns the same number if the number if it's in the Fobonacci sequence
def next_fib(num):
    a = [0, 1, 1]
    b = 1
  
  #keep looping until it is done
    while True:
        if num in a:
            return num
            break
        elif num > b:
            #build up a list of the fibonacci sequence
            b = (a[len(a)-1] + a[len(a)-2])
            a.append(b)
        #in case of negatives
        elif num < b:
            return b
            break

#returns 4 most common digits in a number in decreasing value of the digit
#ties broken on which number comes first
def most_common(num):
    a = str(num)  
    b = list(a)  
    c = []  
    d = []  
    e = []  
    f = 0  
    list_check = []
    
    #make list of digits with their corresponding count
    for g in b:
        if g not in d:
            d.append(g)
            c.append([int(g), b.count(g)])

    #make list of counts
    for h in c:
        if h[1] not in list_check:
            list_check.append(h[1])
            
    #organize the list of counts from greatest to least
    selection_sort(list_check)
    list_check.reverse()
  
    #if there is still less than 4 digits found
    #go through list of digits and count the same number of times as the amount of unique counts starting from highest count
    #results in a list of 4 numbers with counts greatest to least with ties broken by whichever comes first
    for h in list_check:
        for i in c:
            if len(e) < 4:
                if i[1] == h:
                    e.append(i)
  
    #sort list of top 4 digits by the value of the digit
    selection_sort(e)
    e.reverse()

    #construct return value
    for h in e:
        f = f * 10
        f = f + h[0]

    return f 

#finds minimum number of coins using x quarters, y nickles, and z pennies to get to specified number
#returns in format XYZ
def get_coins(num):
    a = num
    b = 0
    c = []
    d = 0

    #divides number by 25(quarters) 
    #rounds down so value of quarters don't pass number
    #leave the remainder for other coins
    b = int(a/25)
    c.append(b)
    a = a - 25*b

    #divides number by 5(nickles)
    #rounds down so value of nickles don't pass remainding amount after quarters
    b = int(a/5)
    c.append(b)
    a = a - 5*b

    #number of pennis is same as remainder
    c.append(a)

    #constructs a return value in form X quarters, Y nickles, and Z pennies
    for i in c:
        d = d * 10
        d = d + i
        
    return d

#--------------------Robot Main Code--------------------#

LF_motor = "56702640167271161404160"
LB_motor = "56702213141711492157531"
RF_motor = "56703126439315218642568"
RB_motor = "56692477276697421313848"
top_motor = "56688344425072198851691"
bottom_motor = "56699702814720378509006"

#sets lift motors to speed
def setliftmotor(speed):
    Robot.set_value(top_motor, "duty_cycle", speed) 
    Robot.set_value(bottom_motor, "duty_cycle", speed)

#sets left motors to speed
def setleftmotor(speed):
    Robot.set_value(LF_motor, "duty_cycle", speed)
    Robot.set_value(LB_motor, "duty_cycle", speed)

#sets right motors to speed    
def setrightmotor(speed):
    Robot.set_value(RF_motor, "duty_cycle", speed)
    Robot.set_value(RB_motor, "duty_cycle", speed)

#stops all motors that move wheels
def stop():
    Robot.set_value(RF_motor, "duty_cycle", 0)
    Robot.set_value(RB_motor, "duty_cycle", 0)
    Robot.set_value(LF_motor, "duty_cycle", 0)
    Robot.set_value(LB_motor, "duty_cycle", 0)
    
#90 degree turn in either direction
def turn(direction):
    if(direction == "L"):
        L = -1
        R = -1
    if(direction == "R"):
        L = 1
        R = 1
    setleftmotor(L)
    setrightmotor(R)
    
#drive robot forward in a unit of distance
def forward(speed):
	setleftmotor(speed)
	setrightmotor(speed * -1)

def fd(distance):
    return distance*1.05
    
def rt(time):
    return time*1.1
   
#make different autonomous modes for different starting zones
#goals, press button, get spoiled candy to other side, end in end zones
def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(alt_left)

def autonomous_main():
    pass

#left default start zone
async def main_left():
    setliftmotor(1)
    await Actions.sleep(0.5)
    setliftmotor(0)
    forward(1)
    await Actions.sleep(fd(1.5))
    stop()
    await Actions.sleep(0.5)
    turn("L")
    await Actions.sleep(rt(1))
    stop()
    await Actions.sleep(0.5)
    forward(1)
    await Actions.sleep(fd(3))
    stop()
    await Actions.sleep(0.5)
    turn("L")
    await Actions.sleep(rt(1))
    stop()

#right default start zone
async def main_right():
    setliftmotor(1)
    await Actions.sleep(0.5)
    setliftmotor(0)
    forward(1)
    await Actions.sleep(fd(3.3))
    stop()
    await Actions.sleep(0.5)
    turn("R")
    await Actions.sleep(rt(1))
    stop()
    await Actions.sleep(0.5)
    forward(1)
    await Actions.sleep(fd(2.1))
    stop()

#left minty fresh start zone
async def alt_left():
    forward(-1)
    await Actions.sleep(fd(0.5))
    stop()
    await Actions.sleep(0.3)
    setliftmotor(0.25)
    await Actions.sleep(0.3)
    setliftmotor(0.1)
    await Actions.sleep(0.5)
    forward(1)
    await Actions.sleep(fd(0.5))
    stop()
    await Actions.sleep(0.5)
    setliftmotor(0.8)
    forward(-1)
    await Actions.sleep(fd(1.7))
    stop()
    await Actions.sleep(0.5)
    turn("R")
    await Actions.sleep(rt(0.85))
    stop()
    await Actions.sleep(0.5)
    forward(1)
    await Actions.sleep(fd(1.9))
    stop()
    await Actions.sleep(0.5)
    setliftmotor(-0.5)
    await Actions.sleep(0.8)
    forward(-1)
    await Actions.sleep(0.85)
    stop()
    setliftmotor(0.2)
    await Actions.sleep(0.5)
    turn("L")
    await Actions.sleep(rt(0.95))
    stop()
    setliftmotor(0)

#left minty fresh start zone
#async def alt_right():

#test autonomous
#async def temp()

def teleop_setup():
    print("yes its running")

def teleop_main():
	#tank control with one joystick
    joystick_x = Gamepad.get_value("joystick_left_x")
    joystick_y = Gamepad.get_value("joystick_left_y")
    A = (100-abs(joystick_x)) * (joystick_y/100) + joystick_y
    B = (100-abs(joystick_y)) * (joystick_x/100) + joystick_x
    R = (A+B)/2
    L = (A-B)/2
    
	#limit values in within +/- 0.9
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
    
	#control lift with one joystick and triggers & bumpers vary speed
    if(abs(Gamepad.get_value("joystick_right_y")) > 0.1):
        if(Gamepad.get_value("r_trigger") == 1):
            setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.2)
        elif(Gamepad.get_value("l_trigger") == 1):
            setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.7)
        elif(Gamepad.get_value("l_bumper") == 1):
            setliftmotor(-1*Gamepad.get_value("joystick_right_y"))
        else:
            setliftmotor(-1*Gamepad.get_value("joystick_right_y")*0.3)
    else:
        setliftmotor(0)
    