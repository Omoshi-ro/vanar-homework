from os import system
system("CLS")
disk = ["home",
        "system",
        "config",
        "backup"
        ]
home_folder = [
    "pictures",
    "music",
    "docs"
    ]
print("/-.")
for i in range(4):
    suf = ""
    if disk[i] == "home":
        suf = " -."
    print("  +--" + disk[i] + suf)
    if disk[i] == "home":
        suf = " -."
        for j in range(3):
            print("  |        +--" + home_folder[j])
            if j < 2:
                print("  |        |")
    if i < 3:
        print("  |")
print()