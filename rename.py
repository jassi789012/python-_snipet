import os

for i in range(0, 100):
    os.rename(f"data/Day{[i+1]}", f"data/Tut{i+1}")
