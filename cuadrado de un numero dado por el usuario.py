#*********zona de funcion*************

def solicitar_numero_1():
    numero_1=float(input("Ingrese el primer numero: "))
    return numero_1
def calcular_cuadrado(numero_1):
    cuadrado=(numero_1**2)
    return cuadrado
def imprimir_resultado(resultado_cuadrado):
    print("La suma de los dos numero es: "+ str(resultado_cuadrado))
    
#***************zona de codigo principal************

numero_1=solicitar_numero_1()
cuadrado=calcular_cuadrado(numero_1)
resultado=imprimir_resultado(cuadrado)