lista = [['a', 'b'], [1, 2, 3]]


def f1(i):
    '''recorre teniendo en cuenta el item'''
    for i in lista:
        for j in i:
            print(j, end=' ')
    print('\n')


def f2(i):
    '''recorre teniendo en cuenta el ienumerate'''
    for i, j in enumerate(lista):
        for j in lista[i]:
            print(j, end=' ')
    print('\n')


def f3(i):
    '''recorre teniendo en cuenta el indice'''
    for i in range(len(lista)):
        for j in lista[i]:
            try:
                for k in lista[i+1]:
                    print(j, k, end=' ')
            except:
                continue
            print('\n')


if __name__ == '__main__':
    f1(lista)
    f2(lista)
    f3(lista)
