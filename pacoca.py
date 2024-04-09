class Objeto():
    def __init__(self, x, y, cor):
        self.__posicao = (x,y)
        self.__rotacao = 0
        self.__cor = cor
        self.__selecionado = False
        self.__escala = (1, 1)

    def display(self):
        pass

    def seleciona(self, x, y):
        pass


from objeto import Objeto

class Circulo(Objeto):
    def __init__(self, x, y, cor, raio):
        super().__init__(x, y, cor)
        self.__raio = raio
    
    def display(self):
        
        pass

from objeto import Objeto

class Poligono_Regular(Objeto):
    def __init__(self, x, y, cor, lados):
        super().__init__(x, y, cor)
    
    def display(self):
        
        pass