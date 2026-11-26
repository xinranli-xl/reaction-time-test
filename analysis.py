import pandas as pd

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

