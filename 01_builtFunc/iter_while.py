lista = [['a', 'b'], [1, 2, 3]]

r = len(lista)
i = 0
while i < r:

    t = len(lista[i])
    i += 1
    
    j = 0
    while j < t:
        print(lista[i-1][j])
        j += 1
