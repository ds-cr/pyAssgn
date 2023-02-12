import unittest
from unittest.mock import patch,Mock
import time

import pyAssgn

class TestpyAssgn(unittest.TestCase):

    def setUp(self):
        self.pyAssgn_obj = pyAssgn.Board_solver()

    @patch('builtins.input', new = Mock(side_effect=['X O X', 'X X X', 'O A X', '']))
    def test_input_fails_when_any_other_value_is_supplied(self):
        print()
        self.assertRaises(Exception, self.pyAssgn_obj.get_input)

    @patch('builtins.input', new = Mock(side_effect=['X O X', 'X X X O', '']))
    def test_input_fails_when_row_length_is_not_same(self):
        print()
        self.assertRaises(Exception, self.pyAssgn_obj.get_input)

    @patch('builtins.input', new = Mock(side_effect=['X','X','']))
    def test_input_fails_when_column_length_not_same_as_row_len(self):
        print()
        self.assertRaises(Exception, self.pyAssgn_obj.get_input)

    @patch('builtins.input', new = Mock(side_effect=['']))
    def test_return_empty_list_when_empty_input_is_given(self):
        print()
        self.pyAssgn_obj.get_input()
        self.pyAssgn_obj.convert_surrounded_O_to_X()
        self.assertListEqual([], self.pyAssgn_obj.get_board())