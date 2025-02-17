

class ClientAction:
    def __init__(self, action):
        self.action = action
    def __str__(self): return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.action)

# All possible actions market can make on an order
#these will be inputs to the machine
ClientAction.sending = ClientAction("order sent by client")
ClientAction.modifying = ClientAction("order modified by client")
ClientAction.cancelling = ClientAction("order cancelled by client")
