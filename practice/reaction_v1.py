import time
import random

print("Press Enter when you see 'go'!")
print("Get ready...")

time.sleep(random.uniform(2, 5))

print("Go!")
start = time.perf_counter()
input()
end = time.perf_counter()

reaction = end - start
print(f"Your reaction time: {round(reaction, 3)} seconds.") 
