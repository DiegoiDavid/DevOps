import Actividad7_1_numeritos   
import act_7_abstract_class  # type: ignore

print("Ingrese un numero")
n = int(input())
enteros = Actividad7_1_numeritos.Numeros(n)
enteros.print_numers()

print("Ingrese un numero racional: ")
q = float(input())
racionales = Actividad7_1_numeritos.Racionales(q)
racionales.print_numeros()

print("Ingrese numero racional para el modulo abstracto:")
m = float(input())
racionales = act_7_abstract_class.Racionales(m)
#racionales = act7_3_abstract_class.AbsNumeros() no puedo instanciar una clase abstract
racionales.print_numeros()