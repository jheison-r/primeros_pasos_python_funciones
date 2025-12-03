#*********************zona de funcion****************

def pedir_distancia_km():
    km=float(input("Digite la distancia en kilometros: "))
    return km
def definir_millas():
    millas=0.621
    return millas
def convertir_millas(km,millas):
    convertir=(km*millas)
    return convertir
def imprimir_resultado(resultado_convertir):
    print("La conversion de kilometros a milllas es: "+str(resultado_convertir))

#*************zona de codigo principal**************

km=pedir_distancia_km()
millas=definir_millas()
convertir=convertir_millas(km,millas)
resultado=imprimir_resultado(convertir)