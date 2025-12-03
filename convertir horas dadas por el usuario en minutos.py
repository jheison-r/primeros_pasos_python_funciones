#****************zona de funcion*************

def pedir_numero_horas():
    horas=float(input("Ingrese la cantidad de horas: "))
    return horas
def convertie_minutos(horas):
    minutos=(horas*60)
    return minutos
def imprimir_resultado(resultado_convertir):
    print("La conversion de horas a minutos es de: "+str(resultado_convertir))

#***********zona de codigo principal*****************

horas=pedir_numero_horas()
minutos=convertie_minutos(horas)
resultado=imprimir_resultado(minutos)