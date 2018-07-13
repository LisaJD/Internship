class State(last_state):
    def __init__(self, orig=None):
        self.turn = ""
        self.movescount = 0
        self.result = "still running"
        self.board = []

class State:
    def __init__(self, last_state=None):
        if last_state is None:
            #self.non_copy_constructor()
            self.turn = ""
            self.movescount = 0
            self.result = "still running"
            self.board = []
        else: self.copy_constructor(last_state)

    def non_copy_constructor(self):
        pass
         # do the non-copy constructor stuff
    def copy_constructor(self, last_state):
        self.turn = last_state.turn
        self.movescount = last_state.movecount
        self.result = last_state.result
        self.board = last_state.board
         # do the copy constructor

    def advanceTurn():
        self.turn += 1

    def emptyCells():
        e_array = []
        for x in range(0, 8):
            if x == 'E':
                e_array.append(x)
                # this won't update when squares get filled though?

    def terminal():
        terminal_moves = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),
            (2,5,8),(0,4,8),(2,4,6)]
        for tuple in terminal_moves:
            if tuple[0]==tuple[1]==tuple[2] and tuple[0]!= 'E'：
                self.result = tuple[0] + 'won'
                return True

    def tie_game(e_array):
        if len(e_array)==0:
            self.result = 'draw'

a=State() # this will call the non-copy constructor
b=State(a) # this will call the copy constructor

# Should be able to implement a number of different strategies
#eg. greedy, etc
class aiPlayer(strategy):
    game = {}

    def minimaxValue(state):
        pass

    def makeMove():
        pass

    def playGame():
        pass

class aiAction(position):
    # where move will place us on board
    self.position = position
    self.minimaxval = 0


    def applyAction(state):
        next = State(position)
        next.board(self.position) = state.turn

    def Applu
