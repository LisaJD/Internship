import random

from engine import MainBoardCoords, SubBoardCoords, SubBoard
from players.stdout import StdOutPlayer
import ms.version
ms.version.addpkg('numpy', '1.14.2')
import numpy as np
import pdb


class MonteCarlo(StdOutPlayer):
    def __init__(self):
        super().__init__() #means: get all initialisation attributes from base class
    def get_my_move(self):  # -> Tuple[MainBoardCoords, SubBoardCoords]
        main_board_coords = self.pick_next_main_board_coords()
        sub_board = self.main_board.get_sub_board(main_board_coords)
        sub_board_coords = self.pick_random_sub_board_coords(sub_board)
        return main_board_coords, sub_board_coords

    def pick_next_main_board_coords(self) -> MainBoardCoords:
        if self.main_board.sub_board_next_player_must_play is None:
            return random.choice(self.main_board.get_playable_coords())
        else:
            return self.main_board.sub_board_next_player_must_play

    @staticmethod
    def pick_random_sub_board_coords(sub_board: SubBoard) -> SubBoardCoords: #this means: argument should be of type 'SubBoard' and
        node = Node(board_state=self.sub_board) #do we need to pass legal moves now so we can make the kids?)
        return monte_carlo_tree_search(node)

import datetime

class Node(object):
    def __init__(self, board_state):
        self.children = []
        self.visited = True
        self.plays = 0
        self.wins = 0
        self.player = 1
        self.board_state = board_state #should be an array storing the game state
        self.CreateChildren()

    def CreateChildren(self):
        print(SubBoard)
        print(SubBoard.get_playable_coords(SubBoard))
        legal_moves = list(self.board_state.get_playable_coords())
        print(legal_moves)
        for move in legal_moves:
            self.children.append(Node(SubBoard.add_my_move(move)))

def monte_carlo_tree_search(node):
    begin = datetime.datetime.utcnow()
    while datetime.datetime.utcnow() - begin < datetime.timedelta(milliseconds=4.9):
        #if all root node's children are visited:
        if all(child.visited for child in node.children):
        #next node to explore is one with max UCT
            return max_uct(node)   #this returns the best poss next move
        #if some unvisited:
        else:
            node.run_simulation(node)
    return max_uct(node)

def run_simulation(node):
    if MainBoard.is_finished: ###
        node.plays += 1 #shouldn't be self.?
        if MainBoard.winner == 1:
            node.wins += 1
            return node.plays, node.wins
        elif MainBoard.winner == 2:
            node.wins -= 1
            return node.plays, node.wins
        else: #draw
            return node.plays #just return result? don't need three if statements
    else:
        next_child = random.choice(node.children)
        node.visited = True
        node.wins = wins + run_simulation(next_child)
        #make this wins, play = ?
def max_uct(node, c=1.4):

    print(node.children)
    uct_vals = [
        (child.wins / (child.plays)) + c * np.sqrt((2 * np.log(node.wins) / (node.plays)))
        for child in node.children
    ] #first terms = ratio wins of child, second term is total ratio wins
    return node.children[np.argmax(uct_vals)]
    #np.argmax returns indices of largest value in array
