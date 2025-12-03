#***************zona de funcion*************

def pedi_base():
    base=float(input("Ingrese la base del triangulo: "))
    return base
def pedir_altura():
    altura=float(input("Ingrese la altura del triangulo: "))
    return altura
def calcular_area(base,altura):
    area=(base*altura)/2
    return area
def imprimir_resultado(resultado_area):
    print("El area de el triangulo es: "+str(resultado_area))

#************zona de codigo principal***************

base=pedi_base()
altura=pedir_altura()
area=calcular_area(base,altura)
resultado=imprimir_resultado(area)