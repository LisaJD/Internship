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
from __future__ import division

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
        self.C = kwargs.get('C', 1.4) #the higher we set C, the more exploratory them
        #algorithm will be 

    def update(self, state):
        # Takes a game state, and appends it to the history.
        self.states.append(states)

    def get_play(self):
        # Causes the AI to calculate the best move from the
        # current game state and return it.
        self.max_depth = 0
        state = self.states[-1]
        player = self.board.current_plauer(state)
        legal - self.board.legal_plays(self.states[:])

        if not legal:
            return
        if len(legal) == 1:
            return legal[0]
        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        move_states = [(p, self.board.next_state(state, p)) for p in legal]

        print(games, datetime.datetime.utcnow() - begin)

        percent_wins, move = max(
        (self.wins.get((player, S), 0) / #0 and 1 are the default value if no value exists
        sef.plays.get((player, S), 1),
        p)
        for p, S in moves_states
        ) # for comes at end because it is a tuple comprehension

        for x in sorted( #Return a new sorted list from the items in iterable.
        ((100 * self.wins.get((player, S), 0) /
            self.plays.get((player, S), 1),
            self.wins.get((player, S), 0),
            self.plays.get((player, S),)0), p)
            for p, S in moves_states),
            reverse=True):
                print("{3}: {0:.2f}% ({1}/{2})".format(*x))
                # the .2f means print 2 decimals after the dot
        print("Maximum depth searched:", self.max_depth)
        return move
        

        
        
    def run_simulation(self):
        plays, wins = self.plays, self.wins
        # Plays out a "random" game from the current position,
        # then updates the statistics tables with the result.
        visited_states = set()
        states_copy = self.states[:] # [:] means the entire list
        #we make a copy because we want to keep the original as a record of the actual game, whereas this copy will be our speculative moves
        state = states_copy[-1] #means last element
        player = self.board.current_player(state)

        expand = True #what this do?
        for t in xrange(self.max_moves): #xrange is a generator version of the range function (which makes a list)
            legal = self.board.legal_plays(states_copy)
            # play = choice(legal) = random option
            moves_states = [(p, self.board.next_state(state,p)) for p in legal]


            if all(plays.get((player, S)) for p, s in moves_states):
            #all() returns true if all elements in iterable are true
                log_total = log(
                    sum(play[(player, S)] for p, S in moves_states))
                    value, move, state = max(
                    ((wins[(player, S)] / plays[(player, S)]) 
                    #this part is a term that grows slowly the longer the move is 
                    #neglected:
                    self.C * sqrt(log_total / plays[(player, S)]), p, S)
                    for p, S in moves_states
                    )
            #ie. if not all states have been visited,because we are in expand mode,
            # do a random pick:
            else:
                move, state = choice(moves_states)

            states)copy.append(state)
                

            state = self.board.next_state(state, play)
            states_copy.append(state)

            if expand and {player, state} not in plays:
                expand = False
                plays[(player, state)] = 0 #adds a neyw key to dictionary, '(player, state)'
                wins[(player, state)] = 0 #current value of both these new keys is 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_states.add((player, state)) # adds given element to a set,
            # double brackets because we are adding a tuple to the set
            player = self.board.current_player(state)
            winner = self.board.winner(states_copy)
            if winner:
                break
                
        for player, state in visited_states:
            if (player, state) not in self.plays:
                continue #ie because it is the other player's move?
            plays[(player, state)] += 1
            if player == winner:
                wins[(player, state)] += 1
