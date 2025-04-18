def guess_number():
    import random

    # guess number between 1 and 100
    attempts = 0
    user_input = ""

    print("Welcome to the Guess the Number game!")
    number = 50
    left, right = 1, 100
    number = left + (right - left) // 2
    while True:
        attempts += 1
        print(f"Your number is {number}?")
        user_input = input("Am I rigth?: ")

        if user_input.lower() == 'yes':
            print(f"Deal! I guess for {attempts}!")
            break
        
        if user_input.lower() == 'more':
            left = number
            number = (left + right) // 2
        elif user_input.lower() == 'less':
            right = number
            number = (left + right) // 2
        else:
            print("Please answer with 'yes', 'more', or 'less'.")
            attempts -= 1
            continue
    print("Game over!")
    print(f"Your number is {number}!")
    print(f"I guessed it in {attempts} attempts!")


if __name__ == "__main__":
    guess_number()
    