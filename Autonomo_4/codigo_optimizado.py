import time
import numpy as np

def buscar_primos_optimizado():
    print("Iniciando busqueda de primos (version optimizada)")

    inicio = time.time()

    limite = 100000

    ###1 numpyy: creamos un array para acelerar las operaciones 
    es_primo = np.ones(limite + 1, dtype=bool)
    ## el 0 y el 1 no son primos
    es_primo[0] = es_primo[1] = False

    ## e. reducir el rango del buvcle iteramos solo hasta la raiz cuadrada de n

    raiz = int(np.sqrt(limite))

    for i in range(2, raiz + 1):
        if es_primo[i]:
            es_primo[i*i:limite+1 : i] = False
    ### 3. List comprehensions. convertimos el array de booleansos en la lista final de numeros

    primos = np.nonzero(es_primo)[0]

    fin = time.time()
    tiempo_total = fin - inicio

    print(f"Total de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecucion: {tiempo_total:.6f} segundos")
if __name__ == "__main__":
    buscar_primos_optimizado()