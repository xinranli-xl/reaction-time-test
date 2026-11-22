import time
import random

def measure_reaction():
    print("Get ready...")

    time.sleep(random.uniform(2, 5))

    print("Go!")
    start = time.perf_counter()
    input()
    end = time.perf_counter()
    return end - start

reaction = measure_reaction()
if reaction < 0.1:
    print("False start! Wait for GO next time.")
else:
    print(f"Your reaction time: {round(reaction, 3)} seconds") 