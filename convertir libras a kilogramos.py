#********zona de funcion**********

def pedir_libras():
    libras= float(input("ingrese las libras que quiere convertir: "))
    return libras
def calcular_kilogramos(libras):
    kilogramos= 0.454
    conversion=(libras * kilogramos)
    return conversion
def imprimir_resultado(resultado_conversion):
    print("La conversion de libras a kilogramos es: ", resultado_conversion)
    
#***********zona de codigo principal**********+
libras=pedir_libras()
conversion= calcular_kilogramos(libras)
kilogramos=imprimir_resultado(conversion)