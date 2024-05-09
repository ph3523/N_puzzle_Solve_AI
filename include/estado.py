class estado:

   def __init__(self, currentState, lastState, direction, depth, cost):
        self.state = currentState
        self.parent = lastState
        self.direction = direction
        self.depth = depth
         
        if lastState:
            self.cost = lastState.cost + cost

        else:
            self.cost = cost
    
    