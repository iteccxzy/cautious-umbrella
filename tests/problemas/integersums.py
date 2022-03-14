'''
Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.
'''


def main():
    try:
        entrada = int(input('ingrese un valor:'))
    except:
        return print(0)
    print(add_it_up(entrada))


def add_it_up(e):    
    r = 0
    for i in range(e+1):
        r += i
    return r


if __name__ == '__main__':
    main()
