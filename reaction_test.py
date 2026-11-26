import time
import random
import os
from datetime import datetime


def measure_reaction():
    print("Get ready...")
    time.sleep(random.uniform(2, 5))
    print("Go!")
    start = time.perf_counter()
    input()
    end = time.perf_counter()
    return end - start

def run_test(rounds):
    times = []

    while len(times) < rounds:
        reaction = measure_reaction()
        if reaction < 0.1:
            print("False start!")
        else:
            times.append(reaction)
            print(f"Round {len(times)}: {round(reaction, 3)} seconds")

    return times


def show_summary(times):
    average = sum(times) / len(times)
    print(f"Average: {round(average, 3)} seconds")
    print(f"Fastest: {round(min(times), 3)} seconds")
    print(f"Slowest: {round(max(times), 3)} seconds")


def save_results(times, filename):
    file_exists = os.path.exists(filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        if not file_exists:
            f.write("timestamp,round,reaction_time\n")
        for i in range(len(times)):
            f.write(f"{timestamp},{i + 1},{round(times[i], 3)}\n")


results = run_test(5)
show_summary(results)
save_results(results, "results.csv")
print("Results saved to results.csv")