#***************zona de funcion*****************
import math
def pedir_numero():
    numero=int(input("Ingrese el numero: "))
    return numero
def calcular_raiz(numero):
    raiz_cuadrada= (math.sqrt(numero))
    return raiz_cuadrada
def imprimir_resultado(resultado_raiz):
    print("La raiz cuadrada del numero es: ", str(resultado_raiz))


#**************zona de codigo principal****************

numero=pedir_numero()
raiz_cuadrada=calcular_raiz(numero)
resultado=imprimir_resultado(raiz_cuadrada)