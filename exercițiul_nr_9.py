from time import sleep
from os import system
laptop_1_model = "Apple MacBook Air 13"
laptop_2_model = "Asus ROG Strix G15 G513RW"
laptop_3_model = "Lenovo IdeaPad 3 15ADA05"

laptop_1_price = 20490, "lei"
laptop_2_price = 38490, "lei" 
laptop_3_price = 7490,  "lei"

laptop_1_rates = 2117, "lei/monthly"
laptop_2_rates = 4494, "lei/monthly"
laptop_3_rates = 744,  "lei/monthly"

print(f"{laptop_1_model} price {laptop_1_price} you can buy it installments with {laptop_1_rates}")
print(f"{laptop_2_model} price {laptop_2_price} you can buy it installments with {laptop_2_rates}")
print(f"{laptop_3_model} price {laptop_3_price} you can buy it installments with {laptop_3_rates}")
sleep(10)
system("CLS")

print("Which laptop whould you like information about?")
print(f"1.{laptop_1_model}")
print(f"2.{laptop_2_model}")
print(f"3.{laptop_3_model}")
choice = int(input("Enter 1, 2, or 3: "))

if choice == 1:
    print("\n\
    Brand                     Apple\n\
    Demesion (L x L x G)      304 x 212 x 16 mm\n\
    Weight                    1.29 kg\n\
    Model Name                MacBook Air 13 2020\n\
    Cod Model                 MGN63RU/A\n\
    Color                     Space Gray\n\
    Graphics Card Description Integrated\n\
    Keyboard                  Ambient light sensor\n\
    Keyboard Language         Română\n\
    Segment                   Ultrabook\n\
    Chip                      Apple M1\n\
    Nr. Core                  8-core CPU\n\
    Display Resolution(px)    2560 x 1600\n\
    Diplay Diagonal           13.3-inch\n\
    Display Type              IPS\n\
    Memory                    8 GB\n\
    Type of Storage           SSD\n\
    Capacity of SSD           255 GB\n\
    Wireless                  Bluetooth 5.0 wireless technology\n\
                              Wi-Fi 802.11ax\n\
    Operating System          macOS\n\
    Battery                   Li-Pol\n\
    Camera                    720p\n\
    Microphone                Yes\n\
    Audio                     Sterio speakers\n\
    Carcass material          Aluminum\n\
    Touch ID                  Yes")
elif choice == 2:
    print("\n\
        Brand                  Asus \n\
        Demesion (L x L x G)   354 x 259 x 27 mm\n\
        Weight                 2.3 kg\n\
        Model Name             ROG Strix G15\n\
        Cod Model              HQ198\n\
        Color                  Eclipse Gray\n\
        Graphics Card          GeForce RTX 3070 Ti\n\
        Graphic Memory         8 GB\n\
        Keyboard               RGB Gaming\n\
        Keyboard Language      Russian\n\
        Segment                Gaming\n\
        Chip                   AMD Ryzen 9\n\
        Nr. Core               8-core CPU\n\
        Display Resolution(px) 2560 x 1440\n\
        Diplay Diagonal        15.6-inch\n\
        Display Type           IPS\n\
        Memory                 16 GB\n\
        Type of Storage        SSD\n\
        Capacity of SSD        512 GB\n\
        Wireless               Bluetooth 5.2 wireless technology\n\
                               Wi-Fi 802.11ax\n\
                               RJ-45 LAN\n\
        Operating System       FreeDos\n\
        Battery                Li-Pol\n\
        Camera                 1080p\n\
        Microphone             Yes\n\
        Audio                  Sterio speakers\n\
        Carcass material       Aluminum\n\
        Touch ID               Yes")
elif choice == 3:   
    print ("\n\
        Brand                  Lenovo\n\
        Demesion (L x L x G)   362.2 x 253.4 x 19.9 mm  \n\
        Weight                 1.85 kg\n\
        Model Name             IdeaPad 3\n\
        Cod Model              15ADA05\n\
        Color                  Gray\n\
        Graphics Card          Integrated\n\
        Keyboard               Plane\n\
        Keyboard Language      English\n\
        Segment                Home and Office\n\
        Chip                   AMD Athlon\n\
        Nr. Core               2-core CPU\n\
        Display Resolution(px) 1366 x 768\n\
        Diplay Diagonal        15.6-inch\n\
        Display Type           IPS\n\
        Memory                 4 GB\n\
        Type of Storage        SSD\n\
        Capacity of SSD        256 GB\n\
        Wireless               Bluetooth 5.0 wireless technology\n\
                               Wi-Fi 802.11ax\n\
        Operating System       FreeDos\n\
        Battery                Li-Pol\n\
        Camera                 Yes\n\
        Microphone             Yes\n\
        Audio                  Speakers\n\
        Carcass material       Aluminum\n\
        Touch ID               No")   
else:
    print("Invalid choice. Please enter 1, 2 or 3.")     

while True:
    buy_laptop = input("Would you like to buy a leptop? (yes or no): ")
    if buy_laptop.lower() == "yes":
        print("Great, let's poriceed to payment!")
        while True:
            if choice == 1:
                print(f"Whole amount of {laptop_1_model} is {laptop_1_price} installment will be {laptop_1_rates}.")
                paymen_option = input("How youd you like to pay? (whole amount or installment): ")
                if paymen_option.lower() ==  "whole amount":
                    print(f"Thank you for your purchase! The {laptop_1_model} will be shipped to you shortly.")
                    break
                elif paymen_option == "installment":
                    print(f"Great the instalment payment of {laptop_1_model} will be {laptop_1_rates}.")
                    break
                else:
                    print("Invalid input. Please enter 'whole amount or instalment'.")
            elif choice == 2:
                print(f"Whole amount of {laptop_2_model} is {laptop_2_price} installment will be {laptop_2_rates}")
                paymen_option = input("How youd you like to pay? (whole amount or installment): ")
                if paymen_option.lower() ==  "whole amount":
                    print(f"Thank you for your purchase! The {laptop_2_model} will be shipped to you shortly.")
                    break
                elif paymen_option == "installment":
                    print(f"Great the instalment payment of {laptop_2_model} will be {laptop_2_rates}.")
                    break
                else:
                    print("Invalid input. Please enter 'whole amount or instalment'.")
            elif choice == 3:
                print(f"Whole amout of {laptop_3_model} is {laptop_3_price} installemnt will be {laptop_3_rates}.")
                paymen_option = input("How youd you like to pay? (whole amount or installment): ")
                if paymen_option.lower() ==  "whole amount":
                    print(f"Thank you for your purchase! The {laptop_3_model} will be shipped to you shortly.")
                    break
                elif paymen_option == "installment":
                    print(f"Great the instalment payment of {laptop_3_model} will be {laptop_3_rates}.")
                    break
        break
    elif buy_laptop.lower() == "no":
        print("Thank you for your time!")
        break
    else:
        print("Invalid input. Enter please yes or no ")