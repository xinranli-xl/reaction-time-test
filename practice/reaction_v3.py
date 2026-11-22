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

def run_test(rounds):
    valid = 0
    total = 0

    while valid < rounds:
        reaction = measure_reaction()
        if reaction < 0.1:
            print("False start!")
        else:
            valid += 1
            total += reaction
            print(f"Round {valid}: {round(reaction, 3)} seconds")

    average = total / rounds
    print(f"Average: {round(average, 3)} seconds")

run_test(2)