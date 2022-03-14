from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('\nsegundo\n')
    print('\nBye', name)


if __name__ == '__main__':
    info('\nPrimero\n')
    p = Process(target=f, args=('Gabriel',))
    p.start()
    p.join()
