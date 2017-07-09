import unittest
import bigger_is_greater


class BiggerIsGreaterTest(unittest.TestCase):

    def setUp(self):
        self.g = bigger_is_greater.BiggerIsGreater()

    # def test_x(self):
    #     gen = self.g.get_next_combination('abc')
    #     next(gen)
    #     self.fail(next(gen))


    def test_get_combinations(self):
        self.assertEqual('acb', self.g.get_combinations('abc'))
        # self.fail(self.g.get_next_combination('abc'))
        self.assertEqual('ba', self.g.get_combinations('ab'))
        # self.fail(self.g.get_combinations('ab'))
        self.assertEqual('no answer', self.g.get_combinations('bb'))
        self.assertEqual('hegf', self.g.get_combinations('hefg'))
        self.assertEqual('dhkc', self.g.get_combinations('dhck'))
        self.assertEqual('hcdk', self.g.get_combinations('dkhc'))
        self.assertEqual(
            'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm',
            self.g.get_combinations('zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw')
        )


