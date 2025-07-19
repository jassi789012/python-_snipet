import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)


hour = int(time.strftime('%H'))

min = int(time.strftime('%M'))

sec = int(time.strftime('%S'))

if(hour<=11 and min<=59 and sec<=59):
    print("Good Morning..")
elif(hour<=16 and min<=59 and sec<=59):
    print("Good Afternoon..")
elif(hour<=20 and min<=59 and sec<=59):
    print("Good Evening..")
else:
    print("Good Night..")

    
    

