Comandos :
Top = Como un administrador de tareas en UBUNTU. (EL primer numero es el PID, elidentificador numerico de ese proceso
Htop = Igual que el top, pero con mas posibilidades como filtrar por nombre, etc ...
Kill = Para eliminar un proceso activo. kill PID.  Ejemplo "kill 3262".








script para consehuir el PID de un proceso
#Script para imprimir el PID (numero de un proceso).
import os
# Obtenemos el PID del proceso actual (el script)
pid = os.getpid()
# Imprimimos el PID
print(f"El PID del script 'bucle_infinito' en 'python.py' es {pid}")
#Posteriormente le haremos in kill a ese PID.









Ahora haremos un hilo, un hilo es un proceso pero que se va haciendo todo el tiempo, no es como un proceso normal, un proceso empieza y acaba, un hilo puede seguir haciendose mientras el otro proceso tambien se hace, es para hacer varias cosas simultaneamente.
Aqui dejo un ejemplo 
import threading
import time

# Función regular que realiza una tarea lenta
def funcion_regular():
    for i in range(3):
        time.sleep(1)  # Simulamos una tarea que toma 1 segundo
        print("Función regular: Tarea completada")

# Función que será ejecutada en un hilo y realiza la misma tarea lenta
def funcion_hilo():
    for i in range(3):
        time.sleep(1)  # Simulamos una tarea que toma 1 segundo
        print("Función en hilo: Tarea completada")

# Ejecutar la función regular en el programa principal
funcion_regular()

# Crear un hilo que ejecuta 'funcion_hilo'
mi_hilo = threading.Thread(target=funcion_hilo)

# Iniciar el hilo
mi_hilo.start()

# Esperar a que el hilo termine antes de finalizar el programa
mi_hilo.join()

print("Programa principal ha terminado")
