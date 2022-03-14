import time

'''defino la lista'''
lista = range(1, 10000)


def main():
    '''defino la funcion generador'''
    def myGen(l):
        for i in l:
            yield i * i

    '''devuelve un objeto generador'''
    a = myGen(lista)

    '''lo recorro con for'''
    for i in a:
        print(i, end='-')


def comprensive():
    '''devuelvo el objeto generador'''
    r = (i * i for i in lista)
    '''lo recorro con next'''
    print(next(r))
    print(next(r))
    print(next(r))


if __name__ == '__main__':
    segundos = time.time()
    main()
    print('\ntiempo: ', time.time() - segundos)

    segundos = time.time()
    comprensive()
    print('\ntiempo: ', time.time() - segundos)
