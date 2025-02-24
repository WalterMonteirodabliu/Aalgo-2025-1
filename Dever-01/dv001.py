import time  
import random 

def quick_sort(arr):
    """
    Implementação do algoritmo Quick Sort utilizando a abordagem recursiva.
    Ele escolhe um pivô, divide a lista em três partes (menores, iguais e maiores) 
    e chama a função recursivamente nas partes menores e maiores.
    """
    if len(arr) <= 1:  # Caso base: se a lista tem 0 ou 1 elemento, já está ordenada
        return arr
    pivot = arr[len(arr) // 2]  # Escolhe o pivô como o elemento do meio
    left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
    middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
    right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
    return quick_sort(left) + middle + quick_sort(right)  # Chama a função recursivamente

def medir_tempo_quick_sort(tamanho):
    """
    Gera uma lista aleatória de números inteiros com o tamanho especificado
    e mede o tempo necessário para ordená-la usando Quick Sort.
    """
    arr = [random.randint(1, 1000000) for _ in range(tamanho)]  # Cria uma lista aleatória com números entre 1 e 1.000.000
    inicio = time.time()  # Captura o tempo antes da execução do Quick Sort
    quick_sort(arr)  # Executa o Quick Sort
    fim = time.time()  # Captura o tempo após a execução do Quick Sort
    return fim - inicio  # Retorna o tempo total de execução


tamanhos = [100, 1_000, 10_000, 100_000]

for tamanho in tamanhos:
    tempo = medir_tempo_quick_sort(tamanho)  # Mede o tempo para o tamanho atual
    print(f"Tamanho da entrada: {tamanho} - Tempo de execução: {tempo:.5f} segundos")  
