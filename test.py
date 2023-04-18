import unittest
import app
from app import app_f, Player


class TestCardGame(unittest.TestCase):

    def test_start_game(self):
        tester = app_f.test_client(self)
        response = tester.get('/start_game')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New game started", response.data)
        
        response = tester.get('/start_game')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"New game started", response.data)

    def test_simulate_game(self):
        p1 = Player(1, "Alice", 0)
        p2 = Player(1, "Bob", 0)
        winner, trace = app.simulate_game(p1, p2)
        self.assertIn(winner, [p1, p2, "Tie"])
    
    def test_reset_game(self):
        tester = app_f.test_client(self)
        response = tester.get('/reset_game')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()