def main():
    counter = 0
    # Вводим имя файла
    file_name = input('Введите имя файла(с расширением): ')

    # Открываем файл для чтения
    file_open = open(file_name, 'r')

    # Цикл для перебора строк
    for line in file_open:
        counter = counter + 1
        print(counter, end='')
        print(')', end=' ')

        # Отсечь символ '\n' c конца строки
        line = line.rstrip('\n')
        print(line)

    # Закрываем файл
    file_open.close()


if __name__ == '__main__':
    main()