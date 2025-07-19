f = open("file.txt", "r")
text = f.read()
print(text)
f.close()


# if file does not exist write will create a new file
# it will rewrite all contant

f = open("file2.txt", "w")
f.write("Hello file 2")
f.close()



# to append in a txt file

f = open("file2.txt", 'a')
f.write("\nHello , i am appending this")
f.close()

#       ^
#       |
# Both are same
#       |
#       v

with open("file2.txt", "a") as f:
    f.write("\nUsing with keyword ")


# line by line file reading
    file = open("file3.txt","r")
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
    file.close()

i = 0
file = open("file4.txt","r")
while True:
    i = i + 1
    line = file.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"Marks of student {i} in maths : {m1}")
    print(f"Marks of student {i} in maths : {m2}")
    print(f"Marks of student {i} in maths : {m3}")


# line by line writing

file = open("file5.txt","w")
line = ["first line\n","second line\n","third line\n"]
file.writelines(line)
file.close()

file = open("file5.txt","a")
line = ["fourth line","fifth line","sixth line"]
for l in line:
    file.write(l + "\n")
file.close()


with open("file6.txt","r") as f:
    
    # move to the tenth byte in the file
    f.seek(10)
    print(f.tell())

    # read next 5 bytes
    data = f.read(5)

    print(data)

    # tell function return the value of seek


with open("file7.txt","w") as f:
    f.write("Hello World")
    # to truncate the total bytes into 3
    f.truncate(5)

with open("file7.txt","r") as f:
    text = f.read()
    print(text)
