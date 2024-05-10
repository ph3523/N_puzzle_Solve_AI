import random


def gerarEstadoInicial(n):
    # Obter estado final
    estadoInicial = list(range(1, n * n))
    estadoInicial.append(0)  # Peça vazia na última posição

    goal = estadoInicial.copy()
    
    # Embaralhar as peças
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
