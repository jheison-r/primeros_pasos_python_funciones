#***************zona de funcion*****************

def pedir_numero_1():
    numero_1=float(input("Ingrese el primer numero: "))
    return numero_1
def pedir_numero_2():
    numero_2=float(input("Ingrese el segundo numero: "))
    return numero_2
def calcular_residuo(numero_1,numero_2):
    residuo=(numero_1 % numero_2)
    return residuo
def imprimir_resultado(resultado_residuo):
    print("El residuo de la division  es: "+str(resultado_residuo))

#**************zona de codigo principal***************

numero_1=pedir_numero_1()
numero_2=pedir_numero_2()
residuo=calcular_residuo(numero_1,numero_2)
resultado=imprimir_resultado(residuo)