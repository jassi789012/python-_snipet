import random

def ret(n):
    if n == 0:
        return "Snake"
    elif n == 1:
        return "Water"
    elif n == 2:
        return "Gun"
    else:
        return "Invalid input"


h = int(input("Choose from snake, water, and gun (0 for snake, 1 for water, 2 for gun) : "))


c = random.randrange(3)

stat = None

if ret(h) == "Invalid input":
    print("Invalid input")
elif h == c:
    stat = "T"
elif h == 0:
    if c == 1:
        stat = "W"
    else:
        stat = "L"
elif h == 1:
    if c == 0:
        stat = "L"
    else:
        stat = "W"
else:
    if c == 0:
        stat = "W"
    else:
        stat = "L"

    

if stat == 'T':
    print(f"you choosed {ret(h)}\ncomputer choosed {ret(c)}")
    print("Tie")
if stat == 'W':
    print(f"you choosed {ret(h)}\ncomputer choosed {ret(c)}")
    print("you won")
elif stat == 'L':
    print(f"you choosed {ret(h)}\ncomputer choosed {ret(c)}")
    print("you loss")