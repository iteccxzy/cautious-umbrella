
def main():

    lista = int(input('ingrese numero: 1 ó 5: \n'))

    match lista:
        case 1:
            print('es el primero')
        case 5:
            print('es el ultimo')


if __name__ == '__main__':
    main()
