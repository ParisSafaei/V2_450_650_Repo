import random

labubus = ["Happy", "Sleepy", "Lucky", "Sweet", "Secret"]

print("Welcome to Labubu Unboxing!")

while True:
    input("\nPress Enter to open your blind box...")

    toy = random.choices(labubus)

    print("Opening your box...")
    print("You got:", toy, "Labubu!")

    if toy == "Secret":
        print("Wow! You found the rare SECRET Labubu!")

    again = input("Open another box? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break