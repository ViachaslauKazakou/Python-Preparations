import time


def timer(count):
    while count > 0:
        print(f"Осталось {count} секунд", end="\r")
        time.sleep(1)
        count -= 1
    print(" " * 20, end="\r")  # Clear the line
    print("Start")


if __name__ == "__main__":
    try:
        count = int(input("Введите количество секунд для обратного отсчета: "))
        timer(count)
    except ValueError:
        print("Ошибка: Введите целое число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")