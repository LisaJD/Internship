
import string
from state import State
from MarketReponse import MarketAction
from OrderManager import OrderManager

class StateT(State):
    def __init__(self):
        self.transitions = None
    def next(self, input):
        if self.transitions.has_key(input):
            return self.transitions[input]
        else:
            raise "Input not supported for current state"


class WaitingForOrders(StateT):
    def run(self):
        print("Market waiting for orders")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            #each operational mode has state transition matric info
            #inside the class definition
            self.transitions = {
             OrderStatus.sent : MarketResponse.new
            }
        return StateT.next(self, input)

class NewOrder(StateT):
    def run(self):
        print("New order waiting for market response")
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            #each operational mode has state transition matric info
            #inside the class definition
            self.transitions = {
             MarketResponse.acked : OrderStatus.acked
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
OrderStatus.waitingfororders = WaitingForOrders()
OrderStatus.sent = Sent()
OrderStatus.modified = Modified()
OrderStatus.cancelled = Cancelled()

moves = map(string.strip,
  open("../mouse/MouseMoves.txt").readlines())
mouseMoves = map(MouseAction, moves)
MouseTrap().runAll(mouseMoves)
