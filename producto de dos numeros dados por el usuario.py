#*********zona de funcion*************

def solicitar_numero_1():
    numero_1=float(input("Ingrese el primer numero: "))
    return numero_1
def solicitar_numero_2():
    numero_2=float(input("Ingrese el segundo numero: "))
    return numero_2
def calcular_producto(numero_1,numero_2):
    producto=(numero_1*numero_2)
    return producto
def imprimir_resultado(resultado_producto):
    print("La suma de los dos numero es: "+ str(resultado_producto))
    
#***************zona de codigo principal************

numero_1=solicitar_numero_1()
numero_2=solicitar_numero_2()
producto=calcular_producto(numero_1,numero_2)
resultado=imprimir_resultado(producto)