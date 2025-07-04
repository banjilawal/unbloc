import unittest

from src.model.board.board import Board
from src.exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        """Test basic board initialization with valid values"""
        board = Board(id=1, row_count=3, column_count=3)
        self.assertIsNotNone(board)
        self.assertEqual(board.row_count, 3)
        self.assertEqual(board.column_count, 3)
        self.assertIsNotNone(board.squares)

    # Rows tests
    def test_valid_rows(self):
        """Test board creation with valid number of num_rows"""
        board = Board(id=1, row_count=3, column_count=3)
        self.assertEqual(board.column_count, 3)

    def test_invalid_rows(self):
        """Test board creation with invalid number of num_rows"""
        with self.assertRaises(InvalidNumberOfRowsError):
            Board(id=1, row_count=-1, column_count=3)

    # Columns tests
    def test_valid_columns(self):
        """Test board creation with valid number of num_columns"""
        board = Board(id=1, row_count=3, column_count=3)
        self.assertEqual(board.columns, 3)

    def test_invalid_columns(self):
        """Test board creation with invalid number of num_columns"""
        with self.assertRaises(InvalidNumberOfColumnsError):
            Board(id=1, row_count=3, column_count=-1)

if __name__ == '__main__':
    unittest.main()