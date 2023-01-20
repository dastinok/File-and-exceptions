


def main():
    # Объявить переменные


    file = input('Введите имя файла: ')

    # Открыть указанный файл для чтения
    infile = open(file, 'r')

    # Первичное чтение
    contents = infile.readline()
    counter = 1

    # Прочитать и показать первые пять строк
    while contents != '' and counter <= 5:
        # Отсечь символ '\n'
        contents = contents.rstrip('\n')
        print(contents)
        contents = infile.readline()
        counter += 1


    infile.close()


if __name__ == '__main__':
    main()