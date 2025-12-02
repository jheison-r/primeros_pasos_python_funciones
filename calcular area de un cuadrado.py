#************zona de funcion*************

def longitud_lado_1():
    lado=8
    return lado

def calcular_area(lado):
    area=(lado**2)
    return area

def imprimir_resultado(resultado_area):
    print("El area del cuadrado es de: " , str(resultado_area))
    

#**********zona de codigo principal**********

lado=longitud_lado_1()
area=calcular_area(lado)
resultado=imprimir_resultado(area)