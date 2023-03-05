from os import system
from time import sleep
dir_up            = - 1
dir_stopped       = 0
dir_down          = 1
building_floors   = 9
building_roof     = True
building_parking  = True
lift_floor        = 1
lift_open         = True
lift_dir          = dir_down  
lift_target_floor = 9
human_floor       = 1
human_in_lift     = True

system("CLS")
#animation
while True:
    human_floor = int(input("Where is the human? "))
    human_in_lift = input("Is human inside lift (y/n)") == "y"
    call_lift = input("Call the lift (y/n)? ") == "y"
    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_floor
        else:
            lift_target_floor = int(input("Where to? "))
    lift_open = False

    if lift_floor < lift_target_floor:
        speed = +1
        lift_dir = dir_up
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = dir_down
    if lift_floor == lift_target_floor:
        speed = 0    
    while True:
        lift_floor += speed

        if lift_floor == lift_target_floor:
            lift_open = True
            lift_dir = dir_stopped
            if not human_in_lift and lift_target_floor == human_floor:
                human_in_lift = True
            elif human_in_lift and lift_target_floor == lift_floor:
                human_in_lift = False
 
        # Render Frame
        system("CLS")
        if building_roof:
            a = "     "
            if lift_floor == building_floors and lift_dir == dir_up:
                a = " ^ "
            elif lift_floor == building_floors and lift_dir == dir_stopped and lift_open:
                a = " < > "
            elif lift_floor == building_floors and lift_dir == dir_down:
                a = " v "
            else:
                a = "     "
            print("---|-----|----")
            print(f" R |{a}|")
        for floor in range(9,0,-1):
            a = "     "
            c = "     "
            t = "     "
            s =""
            if floor == lift_floor +1:
                if lift_dir == dir_down:
                    a="  v  "
                elif lift_dir == dir_up:
                    a="  ^  "
                elif lift_dir == dir_stopped and lift_open:
                    a=" < > "
            elif floor == lift_floor:
                a='|   |'
                t="|---|"
                if human_in_lift:
                    a ="| H |"
            elif floor == lift_floor -1:
                t="|---|"
            elif floor == human_floor:
                    if not human_in_lift:
                        s= "H"
            print(f"---|{t}|----")
            print(f"{floor:^3}|{a}|{s}")
        if building_parking:
            if floor == lift_floor and building_parking:
                t="|---|"
                print(f"---|{t}|----")
            else:
                print("---|     |----")
            print(" P |     |")
            print("---|-----|----")
        sleep(0.5)
        if lift_floor == lift_target_floor:
            break
    sleep(0.5)