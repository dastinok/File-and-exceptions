def main():


    # Открываем файл и читаем
    open_file = open('numbers.txt', 'r')

    # Чтение построчно первой строки
    line = open_file.readline()

    # Ставим счетчик на 0
    count = 0

    # Цикл чтения всех данных
    while line != '':  # Пока линия не равна пустой строке
        count += 1
        line = open_file.readline()

    # Закрываем файл
    open_file.close()

    # Показать количество имен в файле
    print(f'Прочитано, {count}, имен')





if __name__ == '__main__':
    main()