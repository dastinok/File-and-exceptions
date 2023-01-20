
def main():
    file = open('numbers.txt', 'r')

    x = file.read()

    file.close()

    print(x)




if __name__ == '__main__':
    main()