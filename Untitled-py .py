# palabra para imprimir por consola es print 
# 1. tomar datos
nombre_cliente = input("yilber ramirez")
# 2. procesar datos o informacion
mensaje = nombre_cliente + "hola..."
# 3. mostrar resultados (mensajes)
print("hola mundo de python")
print(mensaje)



"""_sumary_esto son comentarios
que se usan para hacer varios
parrafos.........
"""

#estructuras condicionales
#programa para identificar si el num_positivo/num_neutro/num_negativo

print("dijite un numero: ")
numero=int(input())

if numero > 0:
    print ("el numero es positivo." )
elif numero==0:
    print("el numero es neutro." )    
else:
    print("el numero es negativo." )   
    

#realizar un programa que por medio del numero del mes
#indique el nombre del mes que le corresponde el numero 

print("digite un numero del 1 al 12")    
num=int(input())

match num:
    case 1:
        print("enero")
    case 2:
        print("febrero")    
    case 3:
        print("marzo")    
    case 4:
        print("abril")
    case 5:
        print("mayo") 
    case 6:
        print("junio")  
    case 7:
        print("julio") 
    case 8:
        print("agosto") 
    case 9:
        print("septiembre") 
    case 10:
        print("octubre") 
    case 11:
        print("noviembre") 
    case 12:
        print("diciembre") 
                                 
              
 
while True:
    print("digite la letra 'A' para actualizar sistema")
    print("digite la letra 'E' para eliminar catalogo") 
    print("digite la letra 'C' para crear producto")                          
    print("digite la letra 'S' para salir del programa")
    letra=str(input())
    if letra=='S' or letra=='s':
        print("finalizo con exito \n")
        break
    else:
        print("sigue dentro del proceso del DO WHILE \n")
        
       
print("EL DO-WHILE a finalizado \n")  

#realizar un programa que la variable sea diferente a cero
#este pidiendo un valos por consola e indicar si el numero 
#digitado es par o impar  

num=1
while num!=0:
    print("digite un numero: ")
    num=int(input())
    if num%2==0:
        print("el numero es par")
    else:
        print("el numero es impar")
        
print("el programa ha finalizado")    
    
    
    
    
    
    
#estructura del for

""" crear un programa que solicite la cantidad de numeros que el 
    usuario va a digitar y calcular el acomulado de la lista de numeros 
    entrados por consola """
    
    
sum=o # se crea una variable global 
#print("digite la cantidad de numeros para sumar: ")
#cantidad=int(input()) # estar pendiente de los tipos de variantes 

for i in range(0,10,2):
    print("digite el numero" + str(i+1)+": ")
    numero=int(input())
    suma=suma+numero
    
print("la sumatoria total es: "+ str(suma))


suma=0 # se crea una variable global
print("digite la cantidad de numeros para sumar: ")
cantidad=int(input()) # estar pendiente de los tipos

for i in range(cantidad):
    print("digite el numero" + str(i+1)+": ")
    numero=int(input())
    suma=suma+numero
    
    print("la sumatoria total es: "+ str(suma))
    

#crear funciones en python es con la palabra def
# 1.crear funcion->R.D->parametros
# 2.llamar funcion->E.D->argumentos
# 3.raturn funcion->A.D->variable 
        