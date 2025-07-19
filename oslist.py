import os

folders = os.listdir("data")

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


