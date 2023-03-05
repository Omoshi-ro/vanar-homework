from os import system
dir_up           = - 1
dir_stopped      = 0
dir_down         = 1
building_floors  = 9
building_roof    = True
building_parking = True
lift_floor       = 1
lift_open        = False
lift_dir         = dir_down  
human_floor      = 3
human_in_lift    = True

if lift_floor == human_floor and lift_open:
    human_in_lift = True

# Render Frame
system("CLS")
if building_roof:
    print("---|-----|----")
    print(" R |     |")
#print("---|-----|----") În caz cînd roof este False
for floor in range(9,0,-1):
    if floor == lift_floor -1:
        b = "|---|"
    elif floor == lift_floor:
        b = "|---|"
    else:
        b = "     "
    
    print(f"---|{b}|----")
    if floor == human_floor and not human_in_lift:
        h = " H "
    else:
        h = "    "
    if floor == lift_floor + 1:
        if lift_open:
            l= " < > "
        else:
            if lift_dir == dir_up:
                l = "  ^  " 
            elif lift_dir == dir_down:
                l = "  v  "
            elif lift_dir == dir_stopped:
                l= " < > "
    else:
        l = "     "
    if floor == lift_floor:
        if lift_floor and human_in_lift:
            l = "| H |"
        else:
            l = "|   |"
    print(f"{floor:^3}|{l}|{h} ")
if building_parking:
    print("---|     |----")
    print(" P |     |")
    print("---|-----|----")
# print("---|-----|----") În caz cînd parking este False