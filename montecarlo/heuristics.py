import random

from engine import MainBoardCoords, SubBoardCoords, SubBoard
from players.stdout import StdOutPlayer


class Random(StdOutPlayer):
    def __init__(self):
        super().__init__() #means: get all initialisation attributes from base class

    def get_my_move(self):  # -> Tuple[MainBoardCoords, SubBoardCoords]
        main_board_coords = self.pick_next_main_board_coords()
        sub_board = self.main_board.get_sub_board(main_board_coords)
        sub_board_coords = self.pick_heuristics_sub_board_coords(sub_board)
        return main_board_coords, sub_board_coords

    def pick_next_main_board_coords(self) -> MainBoardCoords:
        if self.main_board.sub_board_next_player_must_play is None:
            return random.choice(self.main_board.get_playable_coords())
        else:
            return self.main_board.sub_board_next_player_must_play

    @staticmethod
    def pick_heuristics_sub_board_coords(sub_board: SubBoard) -> SubBoardCoords:
        possible_moves = sub_board.get_playable_coords()
        for move in possible_moves:
            sub_board = sub_board.add_my_move
            opponents_next_pos_moves = sub_board_next_player_must_play.get_playable_coords()
            opps_sub_board = sub_board_next_player_must_play.get_playable_coords()
            if sub_board.is_finished:
                score += 1 #move wins me small board
            elif 
        #next_best_move =
        return random.choice(sub_board.get_playable_coords())

        @staticmethod
        def Minmax():
            for i in range(len(emptycells)):
                cell = emptycell[i]
                cell_score = scoring(cell)
                branch_value = MinMax(cell)
                if branch_value >= current_best_val:
                    current_best_val = branch_value
                    best_move = cell  #or 'i'?

def scoring(cell):
    sub_board = sub_board.add_my_move
    if sub_board.is_finished:
        score += 1 #move wins me small board

            score -= 1 #move wins me large board
    emptycells = sub_board_next_player_must_play.get_playable_coords()
    for cell in emptycells:
        sub_board =
        if sub_board.is_finished:
            score -= 1 #board where i send them can be won by them
        try my move
        if result = borad won by me
            score -= 1 #boadr i send can be won by me
        if other player play -> they win small board
            score += 1 #playing this move I block 2 in a row from the opponent
