def fibo(l):

    a, b = 0, 1
    for i in range(l):
        print(b, end=' ')
        a, b = b, b+a


fibo(10)
