import time

h = int(time.strftime('%H'))
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))

print(h)
print(m)
print(s)

if(h<=11 and m<=59 and s<=59):
    print("Good Morning..")
elif(h<=16 and m<=59 and s<=59):
    print("Good Afternoon..")
elif(h<=20 and m<=59 and s<=59):
    print("Good Evening..")
else:
    print("Good Night..")