from itertools import permutations


class BiggerIsGreater():

    def get_combinations(self, word):
        print(word)
        result = sorted([''.join(x) for x in permutations(word)])
        print(result[result.index(word) + 1])
        if result[0] == result[1]:
            return 'no answer'
        return result[result.index(word) + 1]
