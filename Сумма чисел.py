def main():
    # Объявить переменные
    line = ''
    amount = 0.0
    num = 0.0

    # Открыть файл numbers.txt для чтения
    file_name = open('numbers.txt', 'r')

    # Цикл перебора строк
    for line in file_name:
        num = float(line)
        amount += num + 1

    # Закрываем файл
    file_name.close()

    print('Сумма = ', amount)







if __name__ == '__main__':
    main()