def metodo1():
    a = 1 + 2
    print(a)

def metodo2():
    b = 1 + 3
    print(b)

#Esto de abajo es un ejercicio diferente al de arriba
def suma(numero1, numero2):
    return numero1 + numero2

def Resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

if __name__ == "__main__":
    a = suma(1, 2)
    b = Resta(5, 3)
    c = multiplicacion(4, 2)
    
    print("Resultado de la suma:", a)
    print("Resultado de la resta:", b)
    print("Resultado de la multiplicación:", c)
    
    
    
#Intento de arrays que se escriban abajo diciendo hola
nombres = ["Juanjo", "Pepito", "Salvador"]

for nombre in nombres:
    print(f"Hola, me llamo {nombre}")

    

    
    
    
    
    # Bucle infinito
    
    import time  # Importamos el módulo 'time' para poder usar la función 'sleep'.

def bucle_infinito():  # Definimos una función llamada 'bucle_infinito'.
    while True:  # Iniciamos un bucle 'while' con la condición siempre verdadera, lo que lo hace infinito.
        print("I'm fucking slepping.")  # Imprime un mensaje en cada iteración del bucle.
        time.sleep(5)  # Espera durante 5 segundos antes de la siguiente iteración del bucle.

bucle_infinito()  # Llamamos a la función 'bucle_infinito' para comenzar el bucle infinito.




 

 
 