#*************zona de funcion*************

def definir_longitud():
    longitud=float(input("Ingrese la longitud de la base: "))
    return longitud
def definir_ancho_base():
    ancho=float(input("Ingrese el ancho: "))
    return ancho
def definir_altura():
    altura=float(input("Ingrese la altura: "))
    return altura
def calcular_volumen(longitud, ancho,altura):
    volumen=(1/2 * ancho * altura)* longitud
    return volumen

def imprimir_resultado(resultado_volumen):
    print("El volumen del prisma rectangular es: "+str(resultado_volumen))
    
#**************zona de codigo principal***************

longitud=definir_longitud()
ancho=definir_ancho_base()
altura=definir_altura()
volumen=calcular_volumen(longitud, altura,ancho)
resultado=imprimir_resultado(volumen)
