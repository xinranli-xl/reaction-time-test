name = input("What is your name? ")
fav_int = int(input("What is your favorite integer? "))
hours_slept = float(input("How many hours did you sleep yesterday night? "))

print(f"Hello! Nice to meet you, {name}!")
print(f"The twice of your favorite interger is {fav_int * 2}.")
print(f"If you keep this sleeping schedule, the total sleep hour per week will be {round(hours_slept * 7, 1)}.")
