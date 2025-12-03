#*********zona de funcion*************

def pedir_radio():
    radio=float(input("Ingrese el radio del circulo: "))
    return radio
def definir_pi():
    pi=3.14
    return pi
def calcular_circunferencia(radio,pi):
    circunferencia=(2*pi*radio)
    return circunferencia
def imprimir_resultado(resultado_circunfe):
    print("La circunferencia del circulo es: "+str(resultado_circunfe))

#*************zona de codigo principal****************

radio=pedir_radio()
pi=definir_pi()
circunferencia=calcular_circunferencia(radio,pi)
resultado=imprimir_resultado(circunferencia)