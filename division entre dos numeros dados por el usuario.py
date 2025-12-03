#***************zona de funcion*****************

def pedir_numero_1():
    numero_1=float(input("Ingrese el primer numero: "))
    return numero_1
def pedir_numero_2():
    numero_2=float(input("Ingrese el valor a dividir por el primer numero: "))
    return numero_2
def calcular_division(numero_1,numero_2):
    division=(numero_1 / numero_2)
    return division
def imprimir_resultado(resultado_division):
    print("El resultado de la division es: "+str(resultado_division))

#**************zona de codigo principal***************

numero_1=pedir_numero_1()
numero_2=pedir_numero_2()
division=calcular_division(numero_1,numero_2)
resultado=imprimir_resultado(division)