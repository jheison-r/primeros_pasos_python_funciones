#************+zona de funcion***********

def pedir_longitud_lado():
    lado=float(input("ingrese la longitud del lado: "))
    return lado
def calcular_volumen(lado):
    volumen=(lado**3)
    return volumen
def imprimir_resultado(resultado_volumen):
    print("El volumen del cubo es de : "+str(resultado_volumen))
    
#***********zona de cdigo principal*************

lado=pedir_longitud_lado()
volumen=calcular_volumen(lado)
resultado=imprimir_resultado(volumen)