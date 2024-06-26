import random

def gerarToupeiras():
    matriz = [['-' for _ in range(4)] for _ in range(4)]

    toupeiras_adicionadas = 0
    while toupeiras_adicionadas < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if matriz[i][j] == '-':
            matriz[i][j] = 'T'
            toupeiras_adicionadas += 1

    return matriz

def imprimirMatriz(matriz):
    for linha in matriz:
        print(' '.join(linha))


for geracao in range(1, 4):
    print(f"Geração {geracao}:")
    matriz = gerarToupeiras()
    imprimirMatriz(matriz)
    print()