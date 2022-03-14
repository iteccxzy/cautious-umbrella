'''devuelve un objeto range que se puede iterar con for'''
lista = range(1, 30)


def duplica(i):
    '''recibe de a uno los elementos de map'''
    return i*2


def esPar(l):
    '''recibe de a uno los elemntos de filter'''
    if l % 2 != 0:
        return True


'''
devuelve un ojeto map
'''

resultado = [e * 2 for e in lista]
'''resultado = map(lambda e: e * 2, lista)'''
for i in resultado:
    print(i, end='\t')

print('\n')


resultado2 = [e for e in lista if e % 2 != 0]
''' resultado2 = filter(lambda e: e % 2 != 0, lista)'''
for g in resultado2:
    print(g, end=' - ')
