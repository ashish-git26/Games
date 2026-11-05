import time
import math
a="I Love Python"
for i in range(0,360):
    b=math.radians(i)
    c=math.sin(b)
    print("  " + a)
    time.sleep(0.5)
