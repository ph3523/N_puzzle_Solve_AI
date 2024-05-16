class State:

    def __init__(self, currentState, lastState, direction, depth, cost, goalState):
        self.currentState = currentState
        self.lastState = lastState
        self.direction = direction
        self.depth = depth
        self.goalState = goalState

        if lastState:
            self.cost = lastState.cost + cost
        else:
            self.cost = cost

    def checkGoal(self):
        return self.currentState == self.goalState

    def misplacedTiles(self, n):
        h = 0
        for i in range(n * n):
            if self.currentState[i] != self.goalState[i] and self.currentState[i] != 0:
                h += 1
        return h

    def solution(self):
        solucao = []
        tabuleiros = []
        tabuleiros.append(self.currentState)
        solucao.append(self.direction)
        temp = self.lastState
        while temp.direction:
            solucao.append(temp.direction)
            tabuleiros.append(temp.currentState)
            temp = temp.lastState
        solucao.reverse()
        tabuleiros.reverse()
        return solucao, tabuleiros
    
    #todo: verificar necessidade tonar os metodos abaixo para static
    def availableMoves(self, n):
        moves = []
        i = self.currentState.index(0)
        if i % n > 0:
            moves.append('esquerda')
        if i % n < n - 1:
            moves.append('direita')
        if i - n >= 0:
            moves.append('cima')
        if i + n < n * n:
            moves.append('baixo')
        return moves
    
    def expand(self, n):
        children = []
        nextMoves = self.availableMoves(n)
        for move in nextMoves:
            newState = self.currentState.copy()
            i = newState.index(0)
            if move == 'esquerda':
                newState[i], newState[i - 1] = newState[i - 1], newState[i]
            elif move == 'direita':
                newState[i], newState[i + 1] = newState[i + 1], newState[i]
            elif move == 'cima':
                newState[i], newState[i - n] = newState[i - n], newState[i]
            elif move == 'baixo':
                newState[i], newState[i + n] = newState[i + n], newState[i]
            children.append(State(newState, self, move, self.depth + 1, 1, self.goalState))
        return children