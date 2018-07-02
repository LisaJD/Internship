
import string
from state import State
from OrderManager import OrderManager
from OrderStatus import ClientAction

#This shouldn't be repeated
class StateT(State):
    def __init__(self):
        self.transitions = None
    def next(self, input):
        if self.transitions.has_key(input):
            return self.transitions[input]
        else:
            raise "Input not supported for current state"


class NoOrders(StateT):
    def run(self):
        print("No order yet placed")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            #each operational mode has state transition matric info
            #inside the class definition
            self.transitions = {
             ClientAction.sending : OrderStatus.sent
            }
        return StateT.next(self, input)

class Sent(StateT):
    def run(self):
        print("Order state is SENT")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            #each operational mode has state transition matric info
            #inside the class definition
            self.transitions = {
             ClientAction.modifying : OrderStatus.Modified
             ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class Modified(StateT):
    def run(self):
        print("Order state is MODIFIED")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              ClientAction.modifying : OrderStatus.Modified,
              ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class Cancelled(StateT):
    def run(self):
        print("Order state is CANCELLED. How sad")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
              ClientAction.modifying : OrderStatus.Modified,
              ClientAction.cancelling : OrderStatus.Cancelled
            }
        return StateT.next(self, input)

class OrderStatus(StateMachine):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, OrderStatus.waitingfororders)

# Static variable initialization:
OrderStatus.noorders = NoOrders()
OrderStatus.sent = Sent()
OrderStatus.modified = Modified()
OrderStatus.cancelled = Cancelled()

moves = map(string.strip,
  open("../mouse/MouseMoves.txt").readlines())
mouseMoves = map(MouseAction, moves)
MouseTrap().runAll(mouseMoves)
