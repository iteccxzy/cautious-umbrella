import random
from itertools import combinations


def dameNumeros():
    '''imprime combinaciones de 0 a 40 tomados de a 6'''
    r = list(combinations(range(40), 6))
    print(random.choice(r))
    print(random.choice(r))
    print(random.choice(r))


if __name__ == '__main__':
    dameNumeros()
