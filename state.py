# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:

class State:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

#Base object called State() on which the states will inherit from

# class State(object):
#     """
#     We define a state object which provides some utility functions for the
#     individual states within the state machine.
#     """
#
#     def __init__(self):
#         print('Processing current state:', str(self))
#
#     def on_event(self, event):
#         """
#         Handle events that are delegated to this State.
#         """
#         pass
#
#     def __repr__(self):
#         """
#         Leverages the __str__ method to describe the State.
#         """
#         return self.__str__()
#
#     def __str__(self):
#         """
#         Returns the name of the State.
#         """
#         return self.__class__.__name__

#can call repr(), str(),  or State.__str__
