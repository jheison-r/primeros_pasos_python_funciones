def definir_pi():
    pi=3.14
    return pi

def definir_radio():
    radio= 20
    return radio

def calcular_area(pi, radio,):
    area= (pi*radio**2)
    return area

def imprimir_datos(pi, radio):
    mensaje="El numero pi es: "+pi
    mensaje="El radio es: " +radio
    
    
def imprimir_resultado(resultado_area):
    print("El volumen del cilindro es: " , int(resultado_area))
    
    
#**********************zona de codgo principal****************************

pi=definir_pi()
radio=definir_radio()
area=calcular_area(pi, radio,)
resultado=imprimir_resultado(area)