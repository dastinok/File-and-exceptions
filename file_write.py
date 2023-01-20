# Эта программа пишет три строки данных в файл

def main():
    # Открыть файл names.txt
    outfile = open('names.txt', 'w')

    # Записать имена в файл
    outfile.write('Джон Локк\n')
    outfile.write('Дэвид Хьюм\n')
    outfile.write('Эдмунд Бе\n')


    # Закрыть файл
    outfile.close()






# Вызвать главную функцию
if __name__ == '__main__':
    main()
