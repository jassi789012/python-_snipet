import random

def ret(n):
    if n == 0:
        return "Snake"
    elif n == 1:
        return "Water"
    elif n == 2:
        return "Gun"
    


stat = ['Match Tie','You Win','You Loss'],['You Loss','Match Tie','You Win'],['You Win','You Loss',"Match Tie"]

while True:
    h = int(input("Enter (0 for snake, 1 for water, 2 for gun) : "))

    c = random.randrange(3)

    if h>=0 and h<=2:
        print(f"You choosed : {ret(h)}\nComputer choosed : {ret(c)}")
        print(f"{stat[h][c]}")
    else:
        print("Invalid input")

    again = input("Do you want to play again(yes, no) : ")
    if again == 'no':
        break
