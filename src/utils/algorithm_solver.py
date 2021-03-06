# algorithm_solver.py
# author: Daniel Jauergui
# date: 4-23-2015
import time


class AlgorithmSolver(object):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, board_object):
        """Get the board object and modify it from int array values to string array values, and vice versa
        when returns the board game with new values or the same values if it is stuck.

        Keyword arguments:
        board_object -- Object of Class Board
        return -- Board game with new values or the same values if it is stuck.
        """
        board = board_object.board
        board = [str(numeric_string) for numeric_string in board]

        timestamp = time.clock()
        result = self.algorithm.solve(board)
        timer = str(time.clock() - timestamp)

        if result is not None:
            board = [int(numeric_string) for numeric_string in result]
            if len(board_object.hints) > 1:
                print('\nIt took: ' + timer + ' seconds for SudokuSolver to solve the current game.\n')
                board_object.print_board(board_object.resolved)
                raw_input("\n...(please press any key to continue)")
        else:
            if len(board_object.hints) > 1 and board_object.resolved.count(0) == 0:
                print("\nSudokuSolver cannot solve this board, please see below in solved game and compare: \n")
                board = [int(numeric_string) for numeric_string in board]
                board_object.print_board(board_object.resolved)
                raw_input("\n...(please press any key to continue)")
            elif len(board_object.hints) > 0 and board_object.hints[0] == (0, 0):
                board = [int(numeric_string) for numeric_string in board]
                raw_input("\nThere is not a solution for this board ...(please press any key to continue)")
            else:
                board = [int(numeric_string) for numeric_string in board]
        return board