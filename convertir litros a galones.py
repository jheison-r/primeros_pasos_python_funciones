#********zona de funcion**********

def pedir_litros():
    litros= float(input("ingrese los litros que quiere convertir: "))
    return litros
def calcular_galones(litros):
    galones= 0.264172
    conversion=(litros * galones)
    return conversion
def imprimir_resultado(resultado_conversion):
    print("La conversion de litros a galones es: ", resultado_conversion)
    
#***********zona de codigo principal**********+
litros=pedir_litros()
conversion= calcular_galones(litros)
galones=imprimir_resultado(conversion)