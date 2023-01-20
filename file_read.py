def main():
    infile = open('names.txt', 'r') # Открываем файл

    x = infile.read() # Кидаем открытый файл в переменную

    infile.close() # Закрываем открытый файл

    print(x) # Выводим на экран

if __name__ == '__main__':
    main()