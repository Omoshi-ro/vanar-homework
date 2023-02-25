from os import system
system("CLS")
robot_level     = 5
robot_direction = "down"
robot_has_box   = True 
robot_boxes     = 3

for level in range(10):
    if robot_level -1 == level and robot_direction == "up":
        print("^")
    elif robot_level == level:
        print("x", end="")
        if robot_has_box:
            line = "o"*robot_boxes
            print(line)
        else:
            print(".", end="")
    elif robot_level +1 == level and robot_direction == "down":
        print("v")
    else:
        print(".")