class Infusion:
    def __init__(self,  cantidad_yerba, cantidad_agua):
        '''preparar el mate '''
        self.cantidad_yerba = cantidad_yerba
        self.cantidad_agua = cantidad_agua
        self.estado_yerba = 100

    def cebar(self):
        '''cebar...'''
        self.cantidad_agua -= 10
        self.estado_yerba -= 10

    def get_estado(self):
        return f'queda {self.cantidad_agua}% de agua a {self.temp} Cº y la yerba esta al {self.estado_yerba} %'


class Mate(Infusion):
    def __init__(self, *args):
        '''constructor de la clase mate'''
        self.temp = args[2]
        super().__init__(args[0], args[1])

    def cebar(self, *args):
        super().cebar(*args)
        self.temp -= 5


class Tere(Infusion):
    def __init__(self, *args):
        '''contructor de la clase Tere'''
        self.temp = args[2]
        super().__init__(args[0], args[1])

    def cebar(self, *args):
        super().cebar(*args)
        self.temp += 5


mt = Mate(70, 80, 90)
mt.cebar()
mt.cebar()
mt.cebar()
print(mt.get_estado())

print(vars(mt))

print(issubclass(Mate, Infusion))