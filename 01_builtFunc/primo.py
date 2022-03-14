lista = range(1, 300)


def isPrime(n):
    '''recibe una lista de enteros y devuelve los primos'''
    r = set()
    for num in n:
        if num == 1:
            continue
        elif num == 2:
            r.add(num)
        else:
            for i in range(2, num):
                if num % i == 0:
                    num += 1
        r.add(num)
    for i in r:
        print(i)
        breakpoint()

if __name__ == '__main__':
    isPrime(lista)
