import unittest
from calc import add, subtract

<<<<<<< HEAD

=======
>>>>>>> a7898ee (Add Python CI workflow)
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

<<<<<<< HEAD

if __name__ == "__main__":
    unittest.main()
=======
if __name__ == "__main__":
    unittest.main()
>>>>>>> a7898ee (Add Python CI workflow)
