saludo = ' hola mundo  '


def main():
    saludo2 = saludo.strip()
    saludo3 = saludo.isnumeric()
    saludo4 = saludo.split('o')
    saludo5 = ' * '.join(saludo)

    ''' devuelve un objeto slice'''
    slice2 = slice(1, 5)
    # print(saludo[slice])
    print(saludo5)


if __name__ == '__main__':
    main()
