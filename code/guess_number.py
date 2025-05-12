import random


def guess_number():
    # guess number between 1 and 100
    attempts = 0
    user_input = ""

    print("Welcome to the Guess the Number game!")
    left, right = 1, 100
    number = left + (right - left) // 2
    while True:
        attempts += 1
        print(f"Attempt: {attempts}. Your number is {number}?")
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


def gues2():
    m = 1 #краткая программа без наворотов от 1 до 100.
    p = 100
    z = int(p/2)
    print("загадайте число от 1 до " + str(p))
    count = 0
    for a in range(p):
        count += 1
        if m == z:
            print(f"ваше число: {p} gues for {count} attempts") 
            break
        print(str("ваше число больше " + str(z)))
        a = input('да/нет:')
        if str(a) == str("да"):
            m = z
            z = int((p+m)/2)
        if str(a) == str("нет"):
            p = z
            z = int((p+m)/2)


if __name__ == "__main__":
    # guess_number()
    # gues2()
    start = 1
    end = 5
    print(random.randint(start + 1 , end - 1))
    