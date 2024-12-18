class Aleatorio:
    def __init__(self, semilla):
        self.N_0 = semilla
        self.N_k = self.N_0
        self.__A, self.__B = 7**5, 2**31-1
    def siguiente(self):
        N_k1 = ((self.__A)*self.N_k)%(self.__B)
        self.N_k = N_k1
        return N_k1
    def elegir(self, limite):
        return (self.siguiente())%limite
    

class Regla:
    def __init__(self, izquierda, derecha):
        self.left = izquierda
        self.right = derecha
        self.cont = 1
    def __repr__(self):
        return f"{self.cont} {self.left} -> {' '.join(self.right)}"
    
