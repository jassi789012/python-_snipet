a = input("Enter a : ")
print(f"Table of {a} : ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {(int(a)*i)}")

except:
    print("Invalid Input")


print("important code lines")
print("End of code")


# use of finally keyword

def fun():
    try:
        n = int(input("Enter index : "))
        a = [1,2]
        return 1
    except ValueError:
        print("Given value is not an interger..")
        return 0

    except IndexError:
        print("Invalid Index")
        return 0

    finally:
        print("I will always be executed..")


f = fun()
print(f)


# raising custom errors

a = int(input("Enter any value between 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9 ")

