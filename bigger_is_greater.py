from operator import itemgetter


class BiggerIsGreater():

    def get_combinations(self, word):
        tup1 = self.get_i(word)
        print('tup1', tup1)
        tup2 = self.get_j(tup1, word)
        if tup2 == 'no answer':
            return tup2
        print('tup2', tup2)
        swapped = self.swap(tup1, tup2, word)
        reversed = self.reverse_after_i(tup1, swapped)
        return reversed

    def get_i(self, word):
        result = []
        for i in range(len(word) + 1):
            if i + 1 < len(word) and word[i] < word[i + 1]:
                result.append((i, word[i]))
        print(result)
        if result:
            return max(result, key=itemgetter(0))
        return (len(word) - 1, word[:-1])

    def get_j(self, tup, word):
        result = []
        for j in range(len(word)):
            if j > tup[0] and word[j] > tup[1]:
                result.append((j, word[j]))
        try:
            return max(result, key=itemgetter(0))
        except:
            return 'no answer'

    def swap(self, tup1, tup2, word):
        lst_word = list(word)
        lst_word[tup1[0]], lst_word[tup2[0]] = lst_word[tup2[0]], lst_word[tup1[0]]
        return ''.join(lst_word)

    def reverse_after_i(self, tup1, word):
        first = word[:tup1[0] + 1]
        last = word[tup1[0] + 1:]
        if last:
            return first + last[::-1]
        else:
            return word
