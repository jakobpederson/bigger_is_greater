from itertools import permutations


class BiggerIsGreater():

    def get_combinations(self, word):
        gen = self.get_next_combination(word)
        try:
            result = next(gen)
        except StopIteration:
            return 'no answer'
        # result = sorted([''.join(x) for x in permutations(word)])
        # print(result)
        # if result[0] == result[1]:
            # return 'no answer'
        return result
        # return result[result.index(word) + 1]

    def get_next_combination(self, word):
        for combo in permutations(word):
            if ''.join(combo) > word:
                yield ''.join(combo)

        # for combo in permutations(word):
        #     if ''.join(combo) > word:
        #         yield word
        #     if ''.join(combo) == word:
        #         yield 'no answer'


        # result = sorted([''.join(x) for x in permutations(word) if ''.join(x) > word])
        # if len(result) < 1:
        #     return 'no answer'
        # return result[0]
