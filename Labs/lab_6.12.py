import time
import math

def delayed_sqrt(num, ms):
    time.sleep(ms / 1000)  
    return math.sqrt(num)

num = 25100
milliseconds = 2123

result = delayed_sqrt(num, milliseconds)
print(f"Square root of {num} after {milliseconds} milliseconds is {result}")