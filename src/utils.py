import random
import os
import json

def gerarEstadoInicial(n):
    estadoInicial = list(range(1, n * n))
    estadoInicial.append(0)  # Peça vazia na última posição
    goal = estadoInicial.copy()
    for _ in range(n * n * 10):
        i, j = random.randrange(n * n), random.randrange(n * n)
        estadoInicial[i], estadoInicial[j] = estadoInicial[j], estadoInicial[i]
    return estadoInicial, goal

def qtdInversoes(puzzle):
    inv = 0
    for i in range(len(puzzle) - 1):
        for j in range(i + 1, len(puzzle)):
            if (puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]:
                inv += 1
    return inv

def solucionavel(puzzle):
    inv_counter = qtdInversoes(puzzle)
    if inv_counter % 2 == 0:
        return True
    return False

def printPuzzle(puzzle):
    n = int(len(puzzle) ** 0.5)
    for i in range(0, len(puzzle), n):
        print(puzzle[i: i + n])

def salvarResultado(algoritmo, estadoInicial, resultado, tempo, memoria):
    movimentos = {
        'c': 'Cima',
        'b': 'Baixo',
        'e': 'Esquerda',
        'd': 'Direita'
    }

    if not os.path.exists("resultados"):
        os.makedirs("resultados")

    with open(f"resultados/{algoritmo}.txt", "w") as f:
        if resultado is None:
            f.write(f"Sem resultado utilizando {algoritmo.upper()}\n")
            return

        f.write(f"Tempo de execucao {algoritmo}: {tempo:.4f} segundos\n")
        f.write(f"Resultado {algoritmo}: {', '.join([movimentos[mov] for mov in resultado[0]])}\n")
        f.write(f"Custo {algoritmo}: {resultado[2]}\n\n")
        f.write(f"Memoria utilizada: {memoria} KB\n\n")

        f.write("Passo a passo:\n\n")
        n = int(len(estadoInicial) ** 0.5)
        for i in range(len(estadoInicial)):
            f.write(f"{estadoInicial[i]} ")
            if i % n == n - 1:
                f.write("\n")
        f.write("\n")

        for i in range(len(resultado[1])):
            movimento = movimentos[resultado[0][i]]
            f.write(f"{movimento}\n")
            for j in range(len(resultado[1][i])):
                f.write(f"{resultado[1][i][j]} ")
                if j % n == n - 1:
                    f.write("\n")
            f.write("\n")

        print(f"Arquivo salvo em resultados/{algoritmo}.txt")

def salvarResultadoJson(algoritmo, estadoInicial, resultado, tempo):
    if not os.path.exists("resultados"):
        os.makedirs("resultados")

    data = {
        f"Tempo de execução {algoritmo}": str(tempo),
        f"Resultado {algoritmo}": str(resultado[0]),
        f"Custo {algoritmo}": str(resultado[2]),
        "Estado Inicial": estadoInicial,
        "Passos": []
    }

    for i in range(len(resultado[1])):
        passo = {
            "Ação": str(resultado[0][i]),
            "Estado": resultado[1][i]
        }
        data["Passos"].append(passo)

    with open(f"resultados/{algoritmo}.json", "w") as f:
        json.dump(data, f, indent=4)