import unittest
from bowling_game import Game

class TestScore(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_perfect_game(self):
        # A perfect game is 12 strikes, adding up to 300

        for i in range(0, 12):
            self.game.roll(10)

        final_score = self.game.score()

        self.assertEqual(final_score, 300)


    def test_max_spare_game(self):
        # If you get a 9 and make the spare for every frame,
        # then get a strike at the end, your score is 191

        for frame_num in range(0, 10):
            self.game.roll(9)
            self.game.roll(1)
        # Bonus strike
        self.game.roll(10)

        final_score = self.game.score()

        self.assertEqual(final_score, 191)
        
        
    def test_zero_spare_game(self):
        """A cycle of 0-spare, with a 0 at the end, gives you 100 points""" 

        for i in range(0, 10):
            self.game.roll(0)
            self.game.roll(10)
        self.game.roll(0)

        final_score = self.game.score()

        self.assertEqual(final_score, 100)

    def test_151_game(self):
        self.game.roll(8)
        self.game.roll(2)

        self.game.roll(7)
        self.game.roll(1)

        self.game.roll(10)

        self.game.roll(9)
        self.game.roll(1)

        self.game.roll(8)
        self.game.roll(0)

        self.game.roll(10)

        self.game.roll(7)
        self.game.roll(2)

        self.game.roll(6)
        self.game.roll(4)

        self.game.roll(10)

        self.game.roll(8)
        self.game.roll(2)
        self.game.roll(2)

        final_score = self.game.score()

        self.assertEqual(final_score, 151)

if __name__ == "__main__":
    unittest.main()