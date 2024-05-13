from estado import State
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

def bfs(currentState: State, n: int):
    # Fila de prioridade
    if currentState.currentState == currentState.goalState:
        return currentState

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
                    return filho.solution(), len(explorado)
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
                    return filho.solution(), len(explorado)
                fronteira.put(filho)

    return (("Não foi possível encontrar a solução na profundidade delimitada."), len(explorado))

def aStar():

    return


