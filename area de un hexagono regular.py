#*********zona de funcion¨***********

def pedir_lado():
    lado=float(input("Ingrese el valor del lado: "))
    return lado
def pedir_apotema():
    apotema=float(input("Ingrese el valor del apotema: "))
    return apotema 
def calcular_area(lado,apotema):
    perimetro= 6 * lado
    area=(perimetro*apotema)/2
    return area
def imprimir_resultado(resultado_area):
    print("El area del hexagono regular es de: ", str(resultado_area))
    
#************zona de codigo principal***********

lado=pedir_lado()
apotema=pedir_apotema()
area=calcular_area(lado,apotema)
resultado=imprimir_resultado(area)