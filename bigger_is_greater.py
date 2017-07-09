from itertools import permutations


class BiggerIsGreater():

    def get_combinations(self, word):
        try:
            return min([''.join(x) for x in permutations(word) if ''.join(x) > word])
        except ValueError:
            return 'no answer'
