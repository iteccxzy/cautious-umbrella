
lista = [2, 'hola mundo', [10, 20, 30], {'id': 999}, 2]
lista2 = [19, 32, 43, 84]
lista3 = sorted(lista2, reverse=True)
lista4 = sorted(lista2, key=lambda e: int(str(e)[-1:]))
lista5 = [True, False]
lista6 = lista.copy()
lista7 = list(range(15, 20))
lista8 = [x for x in range(20) if x % 2 != 0]

'''devuelve un objeto enumerate que se puede convertir a lista o recorrer con for'''
lista9 = enumerate(lista)

lista.append('otro string')
lista.extend(lista5)
r = lista.pop()
p = lista.index(True)
lista.insert(2, 'insertado')
lista.reverse()
u = lista.count(2)

print(lista, 'lista', '\n')
print(lista3, 'lista3 ordenada', '\n')
print(lista4, 'lista4 ordenada', '\n')
print(lista6, 'lista6 copia', '\n')
print(lista7, 'lista 7', '\n')
print(lista8, 'lista 8', '\n')
print(list(lista9), 'lista 9', '\n')


print('ultimo elemento:', r, '\n')
print('long de la lista:', len(lista), '\n')
print('indice:', p, '\n')
print('cantidad de veces que repite', u)


del lista
