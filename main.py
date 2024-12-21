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
    

class Gramatica:
    def __init__(self, semilla):
        self.generador_aleatorio = Aleatorio(semilla)
        self.reglas = {}

    def regla(self, izquierda, derecha):
        if izquierda in self.reglas.keys():
            self.reglas[izquierda] = self.reglas[izquierda] + (Regla(izquierda,derecha),)
        else:
            self.reglas[izquierda] = (Regla(izquierda,derecha),)

    def generar(self):
        if 'inicio' in self.reglas.keys():
            return self.generando(('inicio',))
        else:
            raise Exception("No hay regla 'inicio'")
        
    def generando(self, strings):
        resultado = ""
        for string in strings:
            if string not in self.reglas.keys(): #string es simbolo terminal
                nuevo_string = string + " "
                resultado += nuevo_string
            else:
                nueva_tupla = self.seleccionar(string) #string es simbolo no terminal
                nuevo_string = self.generando(nueva_tupla)
                resultado += nuevo_string
        return resultado

    def seleccionar(self,left):
        reglas = self.reglas[left]
        total = 0
        elegido = None

        for regla in reglas:
            total += regla.cont

        indice = self.generador_aleatorio.elegir(total)

        for regla in reglas:
            indice -= regla.cont
            if indice <= 0: 
                elegido = regla
                break

        for regla in reglas:
            if regla != elegido:
                regla.cont += 1

        return elegido.right

        
g = Gramatica(12)

g.regla('inicio',('historia',)) #R1
g.regla('historia',('frase',)) #R2
g.regla('historia',('frase','y','historia')) #R3
g.regla('historia',('frase','sino','historia')) #R4
g.regla('frase',('articulo','sustantivo','verbo','articulo','sustantivo')) #R5
g.regla('articulo',('el',)) #R6
g.regla('articulo',('la',)) #R7
g.regla('articulo',('al',)) #R8
g.regla('sustantivo',('gato',)) #R9
g.regla('sustantivo',('niño',)) #R10
g.regla('sustantivo',('perro',)) #R11
g.regla('sustantivo',('niña',)) #R12
g.regla('verbo',('perseguia',)) #R13
g.regla('verbo',('besaba',)) #R14

cadena = g.generar()
print("Cadena generada: ", cadena)



