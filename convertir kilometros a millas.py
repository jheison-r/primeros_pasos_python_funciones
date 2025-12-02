#*********zona de funcion************

def definir_kilometros():
    kilometros=325
    return kilometros

def definir_factor_conversion():
    factor= 0.62137
    return factor

def combertir_millas(kilometros, factor):
  millas=(kilometros * factor)
  return millas
def imprimir_resultado(resultado_millas):
    print("La conversion de kilometros a millas es: "+str(resultado_millas))
    
#************zona de codigo principal****************

kilometros=definir_kilometros()
factor=definir_factor_conversion()
millas=combertir_millas(kilometros, factor)
resultado=imprimir_resultado(millas)