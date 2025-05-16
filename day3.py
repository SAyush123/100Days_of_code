print("Welcome to the treasure island game!\nYour mission is to find the treasure!")
first = input("Do you want to go left or right?\nType left/right: ").lower()
if first == "right":
    print("You Lose!\nSonic got the treasure before you.")
elif first == "left":
    print("Congrats, You move to the next level!")
    second = input("You need to cross sea you can wait for a ship or cross it by swimming What do you want?\nType Wait/Swim ").lower()
    if second == "swim":
        print("You Lose!\nYou were eaten by shark!")
    elif second == "wait":
        print("Congrats! You made it to next level!")
        third = input("You can dig or search the cave.\nType Dig/Cave ").lower()
        if third == "cave":
            print("You Lose!\nYou were eaten by bear inside cave!")
        elif third == "dig":
            print("🎉 Congratulations! You found the treasure and won the game! 🎉")
else:
    print("Invalid choice. Game Over!")
