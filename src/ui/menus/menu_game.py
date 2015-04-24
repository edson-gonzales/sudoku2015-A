# menu_game.py
# author: Daniel Jauergui
# date: 4-23-2015

from game import *
from board import *
from menu import Menu
from configuration.configuration import *
from file_manager.file_manager import *
from utils.algorithm_solver import *
from solver.algorithms.norvig_solver import NorvigSolver
# from solver.algorithms.backtraking_solver import Backtraking
# from solver.algorithms.bruteforce_solver import Bruteforce

PATH = os.path.dirname(os.path.abspath(__file__))

CONFIGURATION_FILE_PATH = PATH + '..\\..\\..\\configuration\\xml_config.xml'


def display_game_menu(display_main_menu):
    """Sub Menu of Main menu that provide option for user in order to manage the geme.
    It will call display_config_menu function after press any key.
    Define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver - Game Section')
    menu.clear_items()
    menu.add_item((1, 'Start/Continue Game', play_game, 0))
    menu.add_item((2, 'New Game', play_game, 1))
    menu.add_item((3, 'Import Game', display_game_menu, 0))
    menu.add_item((4, 'Export Game', display_game_menu, 0))
    menu.add_item((5, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def play_game(mode=0):
    """This function provide to the user a game interface with menus, board and input request.

    Keyword arguments:
    mode -- Define if game should be generated again or continue with previous status, values (0=ContinueGame,1=NewGame)
    """
    sudoku_game = Game(get_level_configuration())
    board = Board(chr(get_blank_character()))
    if mode == 1 or len(board.board) < 81:
        sudoku_game.generate_game()
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
        board.get_resolved_game()
    option = None
    while option != 'E':
        os.system('cls')
        board.print_ui()
        missing_numbers = len(board.hints)
        print("Missing numbers: %i \n" % missing_numbers)
        if board.board == board.resolved:
            print("Congratulations! you did it. Sudoku solved successfully\n")
        elif board.board.count(0) == 0:
            print("The solution is not correct, pleas see below in solved game an compare:\n")
            board.print_board(board.resolved)
        option = raw_input("Enter coordinates: ")
        if option.upper() == 'N':
            play_game(1)
            break
        elif option.upper() == 'E':
            break
        elif option.upper() == 'B':
            display_game_menu()
            break
        elif option.upper() == 'R':
            board.board = call_algorithm_to_solve(board.board)
        elif option.upper() == 'H':
            board.set_hint()
        else:
            raw_input("Implement movement, please press enter to continue...")


def call_algorithm_to_solve(board):
    algorithm = ""
    code = "algorithm = " + get_algorithm_solver() + "()"
    exec code
    algorithm_to_solve = AlgorithmSolver(algorithm)
    return algorithm_to_solve.solve(board)


def get_level_configuration():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    range_of_level = configuration.level
    range_of_level = range_of_level.split(":")
    try:
        min = range_of_level[1]
        max = range_of_level[2]
    except:
        min = 20
        max = 30
    return min, max


def get_blank_character():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    blank_character = configuration.blank_character
    try:
        blank_character = int(blank_character)
    except:
        blank_character = 42
    return blank_character


def get_algorithm_solver():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    return str(configuration.algorithm)