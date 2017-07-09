from itertools import permutations
from operator import itemgetter


class BiggerIsGreater():

    def get_combinations(self, word):
        try:
            return min([''.join(x) for x in permutations(word) if ''.join(x) > word])
        except ValueError:
            return 'no answer'

    def get_i(self, word):
        result = []
        for i in range(len(word) + 1):
            if i + 1 < len(word) and word[i] < word[i + 1]:
                result.append((i, word[i]))
        if result:
            return max(result, key=itemgetter(1))
        return len(word) - 1

    def get_j(self, tup, word):
        result = []
        for j in range(len(word)):
            if j > tup[0] and word[j] > tup[1]:
                result.append((j, word[j]))
        return max(result, key=itemgetter(1))

    def swap(self, tup1, tup2, word):
        lst_word = list(word)
        lst_word[tup1[0]], lst_word[tup2[0]] = lst_word[tup2[0]], lst_word[tup1[0]]
        return ''.join(lst_word)

