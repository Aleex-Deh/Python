# Ejemplo de un hilo.





import threading
import time

# Función regular que realiza una tarea lenta
def funcion_regular():
    for i in range(3):
        time.sleep(1)  # Simulamos una tarea que toma 1 segundo
        print("Función regular1: Tarea completada")

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

print("Programa principal ha terminado .\n")






print ("Aqui empieza el segundo ejemplo .\n.\n")


# Segundo ejemplo de un hilo, ahora ya no es solo 1 hilo.
# AHora hay un hilo con 3 procesoso dentro, pero aparte simultaneamente, hay otros 3 procesos haciendose.
# Tambien esta pùesto para que no diga el PID de cada proceso.

import threading
import time
import os

# Función que será ejecutada en el hilo
def funcion_hilo():
    for i in range(3):
        print(f"Hilo: Proceso {i+1}, PID {os.getpid()}")
        time.sleep(1)  # Simulamos una tarea que toma 1 segundo

# Función que será ejecutada fuera del hilo
def funcion_fuera_hilo():
    for i in range(3):
        print(f"Fuera del hilo: Proceso {i+1}, PID {os.getpid()}")
        time.sleep(1)  # Simulamos una tarea que toma 1 segundo

# Crear un hilo que ejecuta 'funcion_hilo'
mi_hilo = threading.Thread(target=funcion_hilo)

# Iniciar el hilo
mi_hilo.start()

# Ejecutar 'funcion_fuera_hilo' fuera del hilo
funcion_fuera_hilo()

# Esperar a que el hilo termine antes de finalizar el programa
mi_hilo.join()

print("Programa principal ha terminado")







