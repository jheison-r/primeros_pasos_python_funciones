def definir_pi():
    pi=3.14
    return pi

def definir_radio():
    radio= 20
    return radio

def definir_altura():
    altura= 40
    return altura

 
def calcular_volumen(pi, radio, altura):
    volumen= (1/3*radio**2 * pi * altura)
    return volumen

def imprimir_datos(pi, radio, altura):
    mensaje="El numero pi es: "+pi
    mensaje="El radio es: " +radio
    mensaje="La altura es: "+altura 
    
    
def imprimir_resultado(resultado_volumen):
    print("El volumen del cono es: " , int(resultado_volumen))
    
    
#**********************zona de codgo principal****************************

pi=definir_pi()
radio=definir_radio()
altura=definir_altura()
volumen=calcular_volumen(pi, radio, altura)
resultado=imprimir_resultado(volumen)