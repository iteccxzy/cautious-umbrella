def myDeco(func):
    '''funcion que recibe una funcion'''
    def wrapper(*args):
        '''funcion interna que ejecuta la funcion recibida agrega funcionalidad extra'''
        print('previous---------')
        func(*args)
        print('post-----------')
    return wrapper

def saludo(nombre):
    '''funcion original'''
    print(f'hello, {nombre}')

saludo = myDeco(saludo)

if __name__ == '__main__':
    saludo('gabito')

