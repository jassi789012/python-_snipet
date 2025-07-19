import time

# def fromfor():
#     for i in range(5000):
#         print(i)

# def fromwhile():
#     i = 0
#     while(i<5000):
#         print(i)
#         i = i + 1


# #   time.time()  return the time in seconds
# initial = time.time()
# fromfor()
# t1 = time.time() - initial
# initial = time.time()
# fromwhile()
# t2 = time.time() - initial

# print(f"Time taken by for loop : {t1}")
# print(f"Time taken by while lopp : {t2}")


print(4)
#  time.sleep(n) wait for n seconds

time.sleep(3)
print("This is printed after 3 seconds")

t = time.localtime()
print(t)
formated_time = time.strftime("%y-%m-%d %H:%M:%S")
print(formated_time)