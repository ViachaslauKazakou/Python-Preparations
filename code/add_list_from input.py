def input_data():

    data = []
    while True:
        data_input = input("Введите числа через запятую: ")
        if data_input:
            data.append([int(x)**2 for x in data_input.split(",") if int(x) % 2 == 0])
        else:
            break
    for item in data:
        item.append(sum(item))

    print("Обработанные данные:", data)


if __name__ == "__main__":
    # input_data()


    print(result)

