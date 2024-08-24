import random
import os
import psutil
import json
from time import time
from estado import State


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


def executarERegistrar(algoritmo_nome, algoritmo_func, estado_inicial, estado_final, n, *args):
    process = psutil.Process(os.getpid())
    mem_inicial = process.memory_info().rss / 1024.0
    tempo_inicial = time()

    if algoritmo_nome == "biAStar":
        resultado = algoritmo_func(State(estado_inicial, None, None, 0, 0, estado_final),
                                   State(estado_final, None, None, 0, 0, estado_inicial), n, *args)
    else:
        resultado = algoritmo_func(
            State(estado_inicial, None, None, 0, 0, estado_final), n, *args)

    mem_final = process.memory_info().rss / 1024.0
    tempo_total = time() - tempo_inicial
    salvarResultado(algoritmo_nome, estado_inicial, resultado, tempo_total, mem_final - mem_inicial)
    salvarResultadoJson(algoritmo_nome, estado_inicial, resultado, tempo_total, mem_final - mem_inicial)
    return {
        "algoritmo": algoritmo_nome,
        "tempo": tempo_total,
        "memoria": mem_final - mem_inicial,
        "resultado": resultado
    }


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
        f.write(f"Nos total {algoritmo}: {resultado[2]}\n\n")
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


def salvarResultadoJson(algoritmo, estadoInicial, resultado, tempo, memoria=None):
    if resultado is None:
        resultado_json = {
            "algoritmo": algoritmo,
            "estadoInicial": estadoInicial,
            "resultado": "Sem resultado",
            "tempo": tempo,
            "memoria": memoria
        }
    else:
        resultado_json = {
            "algoritmo": algoritmo,
            "estadoInicial": estadoInicial,
            f"Resultado {algoritmo}": str(resultado[0]),
            f"Nos total {algoritmo}": resultado[2],
            "tempo": tempo,
            "memoria": memoria
        }

    if not os.path.exists("resultadosJson"):
        os.makedirs("resultadosJson")

    with open(f"resultadosJson/{algoritmo}.json", "w") as f:
        json.dump(resultado_json, f, indent=4)

    print(f"Arquivo JSON salvo em resultadosJson/{algoritmo}.json")