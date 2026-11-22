secret = 7

tries = 1

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += tries + 1

    if guess == secret:
        print(f"Correct! You get it in {tries} tries.")
        break
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

while tries > 5:
     print("Game over. The number was 7")