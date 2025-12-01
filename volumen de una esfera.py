def definir_pi():
    pi=3.14
    return pi

def definir_radio():
    radio= 30
    return radio

 
def calcular_volumen(pi, radio):
    volumen= (radio**3 * pi)*4/3 
    return volumen

def imprimir_datos(pi, radio):
    mensaje="El numero pi es: "+pi
    mensaje="El radio es: " +radio
    
    
def imprimir_resultado(resultado_volumen):
    print("El volumen de una esfera de radio 30 es: " , int(resultado_volumen))
    
    
#**********************zona de codgo principal****************************

pi=definir_pi()
radio=definir_radio()
volumen=calcular_volumen(pi, radio)
resultado=imprimir_resultado(volumen)

    

    
