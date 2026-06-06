import random

while True:
    game_level=input("Choose the game level (Easy/Medium/Hard)").lower()
    match game_level:
        case "easy":
            secret=random.randint(1,50)
            Number_range="1 and 50"
        case "medium":
            secret=random.randint(1,100)
            Number_range="1 and 100"
        case "hard":
            secret=random.randint(1,200)
            Number_range="1 and 200"
        case _:
            print("Invalid level! Defaulting to Medium")
            secret = random.randint(1, 100)
            Number_range = "1 and 100"
    tries=0
    List_of_numbers=[]
    while True:
        guess=int(input(f"Guess a number between {Number_range}!\n"))
        diff=abs(secret-guess)
        if diff==0:
            print("\n🎉 Correct!")
        elif diff <=3:
            print("🔥 Very hot! So close")
        elif diff <= 10:
            print("🌡️ Warm! Getting there")
        elif diff <= 20:
            print("❄️ Cold, you're far")
        elif diff <= 50:
            print("🥶 Very cold! Way too far")
        else:
            print("🧊 Frozen! Start over")

        tries+=1
        List_of_numbers.append(guess)
        if guess>secret:
            print("Say smaller!\n")
        elif guess<secret:
            print("say bigger!\n")
        else:
            print(f"""Congratulations! You guessed it in {tries} tries!
🎯 Guessing path: {' → '.join(map(str, List_of_numbers))}
""")

            break
        if tries>9:
            print("=" * 35)
            print("      ☠️ YOU LOST ☠️ ")
            print(f"     Guess: {tries} times")
            print(f"     Number was: {secret}")
            print(f" Guessing path: {' → '.join(map(str, List_of_numbers))}")
            print("       Try again!🎯")
            print("=" * 35)
            break
    play_again=input("do you want to play again?(y/n)").lower()
    if play_again=="n":
        print("goodbye")
        break
