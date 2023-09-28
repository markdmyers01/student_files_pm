"""

    task4_1.py (solution)

"""

from collections import defaultdict


class WordCounter:
    def __init__(self, filepath, min_wordsize=1, max_results=10, encoding='utf-8'):
        self.word_dict = defaultdict(int)
        self.filepath = filepath
        self.min_wordsize = min_wordsize
        self.max_results = max_results
        self.encoding = encoding

    @property
    def min_wordsize(self):
        return self._min_wordsize

    @min_wordsize.setter
    def min_wordsize(self, wordsize):
        self._min_wordsize = wordsize
        if self._min_wordsize <= 0:
            self._min_wordsize = 1

    @property
    def results(self):
        self.word_dict.clear()
        with open(self.filepath, encoding=self.encoding) as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    if len(word) >= self.min_wordsize:
                        self.word_dict[word] += 1

        sorted_dict_items = sorted(self.word_dict.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_dict_items[:self.max_results]


sample_file = '../resources/gettysburg.txt'
counter = WordCounter(sample_file, min_wordsize=5)

# trying a few different min_wordsize values...
counter.min_wordsize = -1
print(counter.min_wordsize)
print(counter.results)

counter.min_wordsize = 'hello'
print(counter.min_wordsize)
print(counter.results)

counter.min_wordsize = 5
print(counter.min_wordsize)
print(counter.results)

