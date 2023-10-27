def metodo1():
    a = 1 + 2
    print(a)

def metodo2():
    b = 1 + 3
    print(b)

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
    
    
    
    nombres = ["Juanjo", "Pepito", "Salvador"]

for nombre in nombres:
    print(f"Hola, me llamo {nombre}")

    
    