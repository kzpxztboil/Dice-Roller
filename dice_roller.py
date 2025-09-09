import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    print("Dice Roller Simulator")
    while True:
        try:
            sides = int(input("Enter the number of sides on the die (minimum 2): "))
            if sides < 2:
                print("A die must have at least 2 sides.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        roll = roll_dice(sides)
        print(f"You rolled a {roll} on a {sides}-sided die.")

        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
