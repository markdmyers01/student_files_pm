"""

    count_module2.py
    Class-based version of the earlier word_count() function.

"""
from collections import defaultdict
import sys


class WordCounter:
    def __init__(self, filepath, min_wordsize=1, max_results=10, encoding='utf-8'):
        self.word_dict = defaultdict(int)
        self.filepath = filepath
        self.min_wordsize = min_wordsize
        self.max_results = max_results
        self.encoding = encoding

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


if __name__ == '__main__':
    sample_file = '../resources/gettysburg.txt'
    results = []
    counter = WordCounter(sample_file, min_wordsize=5)
    try:
        print(counter.results(), counter.word_dict)
    except IOError as err:
        print(f'Error working with file: {err}', file=sys.stderr)
    except UnicodeDecodeError as err:
        print(f'Unrecognized encoding: {err}', file=sys.stderr)
