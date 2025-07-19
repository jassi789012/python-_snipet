from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(6))
print("Done for 6")
print(fx(30))
print("Done for 30")



# it would not take that much time second time due to stored cache
print(fx(20))
print("Done for 20")
print(fx(6))
print("Done for 6")
print(fx(30))
print("Done for 30")
