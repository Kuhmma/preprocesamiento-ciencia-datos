import time

def buscar_primos_sin_optimizar():
    print("Iniciando busqueda de primos (version sin optimizar)")
    
    inicio = time.time()
    primos = []

    ###rangeo de 1 a 100000
    for num in range(1, 100001):
        if num > 1:
            es_primo = True
            
            ###algoritmo no optimizado

            for i in range(2,num):
                if (num % i ) ==0:
                    es_primo = False 
                    break
            if es_primo:
                primos.append(num)
    fin = time.time()
    tiempo_total = fin-inicio

    print(f"Total de primos encontrados: {len(primos)}")
    print(f"Tiempo total de ejecucion: {tiempo_total:.4f} segundos") 

if __name__ == "__main__":
    buscar_primos_sin_optimizar()


    
    