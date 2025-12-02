#**********zona de funcion**********

def solicitar_base():
    base=float(input("Ingrese la base: "))
    return base
def solicitar_altura():
    altura=float(input("Ingrese la altura: "))
    return altura
def calcular_area(base, altura):
    area=(base*altura)
    return area
def imprimir_resultado(resultado_area):
    print("El area del paralelogramo es de: "+str(resultado_area))
    
#**********zona de codigo principal***********

base=solicitar_base()
altura=solicitar_altura()
area=calcular_area(base, altura)
resultado=imprimir_resultado(area)