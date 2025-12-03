#*************zona de funcion************

def solicitar_catidad_dinero():
    dinero=float(input("Digite la cantidad de dinero de la cuenta: "))
    return dinero
def solicitar_cantidad_tiempo():
    tiempo=float(input("Ingrese la cantidad de años: "))
    return tiempo
def definir_tasa_interes():
    interes= 0.05
    return interes
def calcular_tasa(dinero,interes,tiempo):
    tasa=(dinero*interes*tiempo)
    cantidad_total=(dinero+tasa)
    return cantidad_total
def imprimir_resultado(resultado_interes):
    print("La tasa de interes aplicada es: "+str(resultado_interes))


#*************zona de funcion************

dinero=solicitar_catidad_dinero()
interes=definir_tasa_interes()
tiempo=solicitar_cantidad_tiempo()
cantidad_total=calcular_tasa(dinero, interes,tiempo)
resultado=imprimir_resultado(cantidad_total)