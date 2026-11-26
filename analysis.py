import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")
print(df.shape)
print(df["reaction_time"].mean())
print(df["reaction_time"].median())
print(df["reaction_time"].describe())

print(df["reaction_time"]<1.0)
normal = df[df["reaction_time"]<1.0]
print(normal.shape)
print(normal["reaction_time"].mean())

by_run = df.groupby("timestamp")["reaction_time"].mean()
print(by_run)

by_run = df.groupby("round")["reaction_time"].mean()
print(by_run)
by_run_median = df.groupby("round")["reaction_time"].median()
print(by_run_median)

plt.plot(df["reaction_time"])
plt.savefig("reaction_times.png")

plt.plot(df["reaction_time"], marker = "o")
plt.title("Reaction Time Across All Trials")
plt.xlabel("Trial number (5 runs x 5 rounds)")
plt.ylabel("Reaction time (seconds)")
plt.savefig("reaction_times.png")


