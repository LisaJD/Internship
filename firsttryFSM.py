import string

class State(State):
    def __init__(self):
        self.transitions = None
    def next(self, input):
        if self.transitions.has_key(input):
            return self.transitions[input]
        else:
            raise "Input not supported for current state"

class WaitingForOrders(State):
    def run(self):
        print("Engine waiting for orders from client")
    def next(self, input):
        if not self.transitions:
            self.transitions = {
             ClientAction.sent : OrderStatus.NewOrder   
            }
        return StateT.next(self, input)

class NewOrder(State):
    def run(self):
        print("New order waiting for engine response")
    def next(self, input):
        if not self.transitions:
            self.transitions = {
             AtomAction.rejected : OrderStatus.Rejected #this is the case where Atom rejects order, doesn't actually make it to engine but 
             AtomAction.acked : OrderStatus.pendingnew
            }
        return StateT.next(self, input)

class PendingNewOrder(State):
    def run(self):
        print("Order has been acked by engine, waiting to be filled")
    def next(self, input):
        if not self.transitions:
            self.transitions = {
             ClientAction.modifying : OrderStatus.Modified
             ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class ModifiedOrder(State):
    def run(self):
        print("Order state is MODIFIED")
    def next(self, input):
        if not self.transitions:
            self.transitions = {
              ClientAction.modifying : OrderStatus.Modified,
              ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class CancelledOrder(State):
    def run(self):
        print("Order state is CANCELLED. How sad")
    def next(self, input):
        if not self.transitions:
            self.transitions = {
              ClientAction.modifying : OrderStatus.Modified,
              ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class OrderStatus(OrderManager):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, OrderStatus.waitingfororders)

# This is the state machine
class OrderManager:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
    # Template method:
    def runAll(self, inputs):
        for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.run()

# Base class for actions (events)
class Action:
    def __init__(self, action):
        self.action = action
    def __str__(self): 
        return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.action)

# Inherit from base class
class AtomAction(Action):
    pass

class ClientAction(Action):
    pass

# All possible actions client can make on an order
# these will be inputs to the machine (these are the transitions surely)
ClientAction.sending = ClientAction("order sent by client")
ClientAction.modifying = ClientAction("order modified by client")
ClientAction.cancelling = ClientAction("order cancelled by client")
AtomAction.acked = AtomAction("order has been acked by atom") 
AtomAction.pending = AtomAction("order has been part-filled (pending) by atom") 
AtomAction.filled = AtomAction("order has been filled by atom") 
AtomAction.rejected = AtomAction("order has been rejected by atom")

# Static variable initialization:
OrderStatus.waitingfororders = WaitingForOrders() #client not yet sent order
OrderStatus.new = New() #client sent order but not yet been acked or rejected by atom
OrderStatus.pendingnew = PendingNew() #atom (engine) acked the order, waiting to be filled
OrderStatus.modified = Modified() #client modified the order 
OrderStatus.cancelled = Cancelled() #order has been cancelled
OrderStatus.rejected = Rejected() #order has been rejected by atom (engine) --- do we want rejection by atom and by engine to be different?




