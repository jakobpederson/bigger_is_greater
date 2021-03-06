from operator import itemgetter


class BiggerIsGreater():

    def get_min_lexicographically_larger_string(self, word):
        tup1 = self.get_tup1(word)
        tup2 = self.get_tup2(tup1, word)
        if tup2 is None:
            return 'no answer'
        swapped = self.swap_i_and_j(tup1, tup2, word)
        reversed = self.reverse_after_i(tup1, swapped)
        return reversed

    def get_tup1(self, word):
        result = [
            (i, word[i]) for i in range(len(word) + 1)
            if i + 1 < len(word) and word[i] < word[i + 1]
        ]
        if result:
            return max(result, key=itemgetter(0))
        return (len(word) - 1, word[:-1])

    def get_tup2(self, tup, word):
        result = [
            (j, word[j]) for j in range(len(word))
            if j > tup[0] and word[j] > tup[1]
        ]
        try:
            return max(result, key=itemgetter(0))
        except:
            return None

    def swap_i_and_j(self, tup1, tup2, word):
        word_listed = list(word)
        word_listed[tup1[0]], word_listed[tup2[0]] = word_listed[tup2[0]], word_listed[tup1[0]]
        return ''.join(word_listed)

    def reverse_after_i(self, tup1, word):
        first = word[:tup1[0] + 1]
        last = word[tup1[0] + 1:]
        if last:
            return first + last[::-1]
        else:
            return word
