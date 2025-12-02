#********zona de funcion**********

def pedir_pulgadas():
    pulgadas= float(input("ingrese las pulgadas que quiere convertir: "))
    return pulgadas
def calcular_centimetros(pulgadas):
    centimetros= 2.54
    conversion=(pulgadas * centimetros)
    return conversion
def imprimir_resultado(resultado_conversion):
    print("La conversion de pulgadas a centimetros es: ", resultado_conversion)
    
#***********zona de codigo principal**********+
pulgadas=pedir_pulgadas()
conversion= calcular_centimetros(pulgadas)
centimetros=imprimir_resultado(conversion)