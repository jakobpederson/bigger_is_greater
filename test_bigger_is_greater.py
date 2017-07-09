import unittest
import bigger_is_greater


class BiggerIsGreaterTest(unittest.TestCase):

    def setUp(self):
        self.g = bigger_is_greater.BiggerIsGreater()

    def test_get_combinations(self):
        self.assertEqual('acb', self.g.get_combinations('abc'))
        self.assertEqual('ba', self.g.get_combinations('ab'))
        self.assertEqual('no answer', self.g.get_combinations('bb'))
        self.assertEqual('hegf', self.g.get_combinations('hefg'))
        self.assertEqual('dhkc', self.g.get_combinations('dhck'))
        self.assertEqual('hcdk', self.g.get_combinations('dkhc'))
        self.assertEqual(
            'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm',
            self.g.get_combinations('zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw')
        )

    def test_get_i(self):
        self.assertEqual('a', self.g.get_i('ab')[1])
        self.assertEqual('c', self.g.get_i('cdb')[1])

    def test_j(self):
        self.assertEqual((2, 'c'), self.g.get_j(self.g.get_i('abc'), 'abc'))

    def test_swap(self):
        self.assertEqual('bac', self.g.swap((0, 'a'), (1, 'b'), 'abc'))

    def test_reverse_after_i(self):
        self.assertEqual('abfedc', self.g.reverse_after_i((1, 'b'), 'abcdef'))

