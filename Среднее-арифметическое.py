def main():
    # Объявить переменные
    tot = 0
    num = 0
    count = 0

    # Открываем файл для чтения
    file_open = open('numbers.txt', 'r')


    # Перебироаем строки и делаем из них целое число
    for l in file_open:
        count = count + 1 # Счетчик чисел
        num = float(l)
        tot = tot + num # Общее кол-во

    # Закрываем файл
    file_open.close()

    # Считаем среднее-арифметическое
    average = tot / count

    print(f'Средне-арифметическое = {average}')







if __name__ == '__main__':
    main()