```# time up counter 

import time

seconds = int(input("Enter the number of seconds: "))

# Countdown loop
while seconds > 0:
    print(seconds)
    time.sleep(1)   # Wait for 1 second
    seconds -= 1    # Reduce the seconds by 1

print("Time's up!")
```
