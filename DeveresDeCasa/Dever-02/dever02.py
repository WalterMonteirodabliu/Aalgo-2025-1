import time

def fatorial(n): # Função para calcular o fatorial de um número de maneira recursiva 
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Lista de números
numero = [10, 100, 500, 1000]

# Calculando e exibindo o fatorial para cada número da lista
for n in numero:
    tempo_inicial = time.time()  # Registra o tempo de início
    resultado = fatorial(n) # Calcula o fatorial
    tempo_final = time.time()  # Registra o tempo final
    print(f"O fatorial de {n} é {resultado}")
    print(f"O tempo necessário foi {tempo_final - tempo_inicial:.6f} segundos")
