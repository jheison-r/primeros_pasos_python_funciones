#*********zona de funcion*************

def solicitar_numero_1():
    numero_1=float(input("Ingrese el primer numero: "))
    return numero_1
def solicitar_numero_2():
    numero_2=float(input("Ingrese el segundo numero: "))
    return numero_2
def calcular_suma(numero_1,numero_2):
    suma=(numero_1+numero_2)
    return suma
def imprimir_resultado(resultado_suma):
    print("La suma de los dos numero es: "+ str(resultado_suma))
    
#***************zona de codigo principal************

numero_1=solicitar_numero_1()
numero_2=solicitar_numero_2()
suma=calcular_suma(numero_1,numero_2)
resultado=imprimir_resultado(suma)