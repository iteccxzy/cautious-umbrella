def verificaParametros(i=None, *args, **kwargs):
    ''' Print parameters and see the values '''
    print(i, args, kwargs)


def main():
    verificaParametros()
    verificaParametros(5)
    verificaParametros(5, 3, 9)
    verificaParametros(5, 3, u=9)


if __name__ == '__main__':
    main()
