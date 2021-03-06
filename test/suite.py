
# suite.py
# author: Josue Mendoza
# date: 4-30 -2015

import unittest
import sys

sys.path.append("../src")
sys.path.append("../src/file_manager")
sys.path.append("../src/configuration")
sys.path.append("../src/solver")
sys.path.append("../src/solver/algorithms")
sys.path.append("../src/utils")

from file_manager_test import FileManagerTest
from configuration_test import ConfigurationTest
from norvig_solver_test import NorvigSolverTest
from Fallin_solver_test import FallingSolverTest
from data_converter_test import DataConverterTest
from game_test import GameTest

# Load Tests
file_manager_suite = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
configuration_suite = unittest.TestLoader().loadTestsFromTestCase(ConfigurationTest)
norvig_solver_suite = unittest.TestLoader().loadTestsFromTestCase(NorvigSolverTest)
Fallin_solver_suite = unittest.TestLoader().loadTestsFromTestCase(FallingSolverTest)
data_converter_suite = unittest.TestLoader().loadTestsFromTestCase(DataConverterTest)
game_suit = unittest.TestLoader().loadTestsFromTestCase(GameTest)

# Load Test Suite

all_tests = unittest.TestSuite([file_manager_suite, configuration_suite, norvig_solver_suite,
								Fallin_solver_suite,data_converter_suite, game_suit])
# Execute Test Suite
unittest.TextTestRunner(verbosity=2).run(all_tests)