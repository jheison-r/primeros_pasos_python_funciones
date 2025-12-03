#*****************zona funcion*************

def pedir_longitud():
    longitud=float(input("Ingrese la longitud del rectangulo: "))
    return longitud
def pedir_ancho():
    ancho=float(input("Ingrese el ancho del rectangulo: "))
    return ancho
def calcular_area(longitud,ancho):
    area=(longitud*ancho)
    return area
def imprimir_resultado(resultado_area):
    print("El area del rectangulo es: "+str(resultado_area))

#**************zona de codigo principal***************

longitud=pedir_longitud()
ancho=pedir_ancho()
area=calcular_area(longitud,ancho)
resultado=imprimir_resultado(area)