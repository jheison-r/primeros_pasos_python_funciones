#**********zona de funcion**************

def pedir_numero():
    numero=float(input("Ingrese el numero: "))
    return numero
def determinar_par_impar(numero):
    if numero % 2==0:
        return "par"
    else:
        return "impar"
def imprimir_resultado(resultado_numero):
    print("El numero es: "+str(resultado_numero))

#*********zona de codigo principal************

numero=pedir_numero()
determinar=determinar_par_impar(numero)
resultado=imprimir_resultado(determinar)
