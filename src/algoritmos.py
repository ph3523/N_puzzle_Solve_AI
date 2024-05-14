from estado import State
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
# from memory_profiler import profile

# @profile
def bfs(currentState: State, n: int):
    # Fila de prioridade
    if currentState.currentState == currentState.goalState:
        return currentState.solution(), 0

    fronteira = Queue()
    fronteira.put(currentState)
    explorado = set()

    while not fronteira.empty():
        estado = fronteira.get()
        explorado.add(tuple(estado.currentState))

        noFilho = estado.expand(n)
        for filho in noFilho:
            if tuple(filho.currentState) not in explorado:
                if filho.checkGoal():
                    resultado = filho.solution()
                    return resultado[0], resultado[1], len(explorado)
                fronteira.put(filho)
    return

def dfs(currentState: State, n: int):
    # Fila Last In First Out(LIFO)
    if currentState.currentState == currentState.goalState:
        return currentState
    
    fronteira = LifoQueue()
    fronteira.put(currentState)
    explorado = set()

    while not fronteira.empty():
        estado = fronteira.get()
        max_profundidade = estado.depth
        explorado.add(tuple(estado.currentState))

        if max_profundidade == 30:
            continue

        noFilho = estado.expand(n)
        for filho in noFilho:
            if tuple(filho.currentState) not in explorado:
                if filho.checkGoal():
                    resultado = filho.solution()
                    return resultado[0], resultado[1], len(explorado)
                fronteira.put(filho)
    print("Não foi possível encontrar uma solução utlizando DFS")
    return 

def aStar():

    return


