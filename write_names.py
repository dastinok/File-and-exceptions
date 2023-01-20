def main():
    print('Введите имена своих друзей')

    name1 = input('Друг 1: ')
    name2 = input('Друг 2: ')
    name3 = input('Друг 3: ')

    my_file = open('friends.txt', 'w')

    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')

    my_file.close()
    print('Имена были записаны в friends.txt')




if __name__ == '__main__':
    main()