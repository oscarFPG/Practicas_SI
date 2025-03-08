
class State:

    def __init__(self):
        self._current = None
        self._next = None

    def execute(self, perceptions):
        return -1, -1
    
    def nextState(self):
        return