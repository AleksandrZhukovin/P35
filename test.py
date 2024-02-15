import unittest


def square(a, b):
    return a * b


class SquareTest(unittest.TestCase):
    def test_positiv_values(self):
        res = square(2, 3)  # 6
        self.assertEqual(6, res)

    def test_nagative_values(self):
        res = square(-1, -2)
        self.assertEqual(0, res)

    def test_mixed_values(self):
        res = square(-1, 2)
        self.assertEqual(0, res)


def test_positiv_values1():
    res = square(2, 3)
    assert res == 6


def test_nagative_values():
    res = square(2, 3)
    assert res >= 0
#  написати функцію обрахунку площі та довжини кола (radius ** 2 * 3.14) (radius * 2 * 3.14)
