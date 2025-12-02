#*************zona de funcion*************

def definir_longitud_base():
    longitud= 30
    return longitud
def definir_ancho_base():
    ancho=20
    return ancho
def definir_altura():
    altura=40
    return altura
def definir_area_base(longitud):
    area_base=(longitud**2)
def calcular_volumen(area_base, altura):
    volumen=(area_base * altura)/3
    return volumen

def imprimir_resultado(resultado_volumen):
    print("El volumen de la piramide es de: "+str(resultado_volumen))
    
#**************zona de codigo principal***************

longitud=definir_longitud_base()
ancho=definir_ancho_base()
altura=definir_altura()
area_base=definir_area_base(longitud)
volumen=calcular_volumen(area_base, altura)
resultado=imprimir_resultado(volumen)
