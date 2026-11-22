def play_game(secret, max_tries):
    tries = 0

    while True:
         guess = int(input("Guess a number between 1 and 10: "))
         tries += 1

         if guess == secret:
             print(f"Correct! You get it in {tries} tries.")
             break
         elif tries == max_tries:
             print(f"Game over. The number was {secret}.")
             break
         elif guess < secret:
             print("Too low, try again.")
         else:
             print("Too high, try again.")

play_game(7, 5)

