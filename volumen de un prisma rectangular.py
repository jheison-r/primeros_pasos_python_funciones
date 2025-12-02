#****************zona de funcion*********

def definir_longitud():
    longitud= 30
    return longitud
def definir_ancho():
    ancho= 20
    return ancho
def definir_altura():
    altura=40
    return altura
def calcular_volumen(longitud, ancho, altura):
  volumen=(longitud * ancho * altura)
  return volumen
def imprimir_resultado(resultado_volumen):
  print("El volumen del prisma rectangular es de: " +str(resultado_volumen))
  
  
#*************zona de codigo principal**************

longitud=definir_longitud()
ancho=definir_ancho()
altura=definir_altura()
volumen=calcular_volumen(longitud, ancho, altura)
resultado=imprimir_resultado(volumen)