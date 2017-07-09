import unittest
import bigger_is_greater


class BiggerIsGreaterTest(unittest.TestCase):

    def setUp(self):
        self.g = bigger_is_greater.BiggerIsGreater()

    def test_get_min_lexicographically_larger_string(self):
        self.assertEqual('acb', self.g.get_min_lexicographically_larger_string('abc'))
        self.assertEqual('ba', self.g.get_min_lexicographically_larger_string('ab'))
        self.assertEqual('no answer', self.g.get_min_lexicographically_larger_string('bb'))
        self.assertEqual('hegf', self.g.get_min_lexicographically_larger_string('hefg'))
        self.assertEqual('dhkc', self.g.get_min_lexicographically_larger_string('dhck'))
        self.assertEqual('hcdk', self.g.get_min_lexicographically_larger_string('dkhc'))
        self.assertEqual(
            'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm',
            self.g.get_min_lexicographically_larger_string('zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw')
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

