import io
import sys
import os
import unittest
from unittest.mock import patch

# ensure repo root is on sys.path so `import game` works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import game

class TestPlayFunction(unittest.TestCase):
    def test_tie_full_word(self):
        result = game.play('rock', 'rock')
        self.assertEqual(result, "It's a tie!")
        
    def test_tie_abbrev_vs_word(self):
        result = game.play('r', 'rock')
        self.assertEqual(result, "It's a tie!")

    def test_user_wins_full_words(self):
        result = game.play('paper', 'rock')
        self.assertEqual(result, "You win!")

    def test_user_wins_with_abbrev(self):
        result = game.play('p', 'rock')
        self.assertEqual(result, "You win!")

    def test_computer_wins(self):
        self.assertEqual(game.play('s', 'rock'), "Computer wins!")

    def test_computer_wins(self):
        self.assertEqual(game.play('scissors', 'rock'), "Computer wins!")

    def invalid_choice_test(self):
        self.assertEqual(game.play('lizard', 'rock'), "Invalid choice. Please try again.")

    # def test_invalid_choice_returns_empty_and_prints_message(self):
    #     fake_out = io.StringIO()
    #     with patch('sys.stdout', new=fake_out):
    #         result = game.play('x', 'rock')
    #     self.assertEqual(result, "")
    #     self.assertIn("Invalid choice", fake_out.getvalue())

    # def test_quit_raises_systemexit_and_prints_goodbye(self):
    #     fake_out = io.StringIO()
    #     with patch('sys.stdout', new=fake_out):
    #         with self.assertRaises(SystemExit):
    #             game.play('q', 'rock')
    #     self.assertIn("Thanks for playing! Goodbye!", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()