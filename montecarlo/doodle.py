class Board(object):
    def start(self):
        # Returns a representation of the starting state of the game.
        pass

    def current_player(self, state):
        # Takes the game state and returns the current player's
        # number.
        pass

    def next_state(self, state, play):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        pass

    def legal_plays(self, state_history):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        pass

    def winner(self, state_history):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        pass
    
import datetime
from random import choice

class MonteCarlo(object):
    
    def __init__(self, board, **kwargs): 
        # Takes an instance of a Board and optionally some keyword
        # arguments.  Initializes the list of game states and the
        # statistics tables.
        seconds = kwargs.get('time', 30) #if args passed to **kwargs, they get put in a dictionary
        self.calculation_time = datetime.timedelta(seconds=seconds)
        self.board = board
        self.states = []
        self.max_moves = kwargs.get('max_moves', 100)
        self.wins = {}
        self.plays = {}

    def update(self, state):
        # Takes a game state, and appends it to the history.
        self.states.append(states)

    def get_play(self):
        # Causes the AI to calculate the best move from the
        # current game state and return it.
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()

    def run_simulation(self):
        # Plays out a "random" game from the current position,
        # then updates the statistics tables with the result.
        visited_states = set()
        states_copy = self.states[:] # [:] means the entire list
        #we make a copy because we want to keep the original as a record of the actual game, whereas this copy will be our speculative moves
        state = states_copy[-1] #means last element
        player = self.board.current_player(state)

        for t in xrange(self.max_moves): #xrange is a generator version of the range function (which makes a list)
            legal = self.board.legal_plays(states_copy)
            play = choice(legal)
            state = self.board.next_state(state, play)
            states_copy.append(state)

            winner = self.board.winner(states_copy)
            if winner:
                break
