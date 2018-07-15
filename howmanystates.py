import pdb

class State(object):

    transition_matrix = { 'state.INIT' : ('state.CREATED', 'state.REJECTED'),
    'state.CREATED': ('state.ACKED', 'state.REJECTED', 'state.CANCELLED', 'state.PENDING_CANCEL'),
    'state.PENDING_ACK': ('state.ACKED', 'state.REJECTED', 'state.PENDING_CANCEL', 'state.PENDING_REPLACE'),
    'state.ACKED': ('state.CANCELLED', 'state.PENDING_REPLACE', 'state.PENDING_CANCEL', 'state.REJECTED'),
    'state.PENDING_REPLACE': ('state.REPLACED', 'state.ACKED', 'state.PENDING_REPLACE', 'state.PENDING_ACK', 'state.PENDING_CANCEL', 'state.REJECTED'),
    'state.PENDING_CANCEL': ('state.CANCELLED', 'state.PENDING_REPLACE', 'state.REPLACED', 'state.ACKED', 'state.PENDING_ACK', 'state.REJECTED'),
    'state.REPLACED': ('state.ACKED'),
    'state.REJECTED': (''),
    'state.CANCELLED': ('')
    }

    def __init__(self, depth, current_state):
        self.depth = depth
        self.current_state = current_state
        self.possible_states = self.transition_matrix[self.current_state]
        self.next_states = []
        #self.getNextStates() #Why does it only not work here???

    def getNextStates(self):
        if self.depth < 6:
            for i in range(len(self.possible_states)):
                self.next_states.append( State(self.depth + 1, self.possible_states[i]))

if __name__ == '__main__':
    state = State(1, 'state.INIT')
    state.getNextStates()
