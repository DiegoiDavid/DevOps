class Numeros:
    def __init__(self, n):
        self.n = n

        def print_numeros(self):
            for number in range(self.n):
                if((self.n%2)==0):
                    print("El numero es:", number)
                else:
                    print("El cuadro del numero es", number**2)

class Racionales(Numeros):
    def __init__(self,n):
        super().__init__(n)

    def print_numeros(self):
        print("El numero racional es: ", self.n)
        print("El numero racional es forma de fraccion es:", self.n.as_integer_ratio())
        