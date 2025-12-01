def definir_dolares():
    dolares=40
    return dolares

def tasa_de_cambio():
    tasa_cambio= 1.47
    return tasa_cambio

def convertir_euros(dolares, tasa_cambio):
    euros= (dolares * tasa_cambio)
    return euros

def imprimir_datos(dolares):
    mensaje="La cantidad de dolares es de: "+dolares
    
def imprimir_resultado(resultado_dolar):
    print("la convercion de dolares a euros es de: " +str(resultado_dolar))
    
    
#****************zona de codigo principal****************
dolares=definir_dolares()
euros=convertir_euros(dolares)
resultado=imprimir_resultado(dolares)