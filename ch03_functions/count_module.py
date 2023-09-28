"""

    count_module.py
    word_counter() function illustrating keyword and positional arguments.

"""
from collections import defaultdict
import re
import sys


def word_counter(filepath, min_wordsize=1, max_results=10, encoding='utf-8-sig'):
    """
                Accepts a filename and returns a list of tuples of the most frequent
                word occurrences in the file:  \n
                word_counter(filename)                           returns top 10 of all words   \n
                word_counter(filename, 5)                        returns top 10 of 5-letter or more words  \n
                word_counter(filename, 5, 20)                    returns top 20 of 5-letter or more words  \n
                word_counter(max_results=20, filepath=filename, min_wordsize=3)      returns top 20 of 3-letter or more words \n

        :param filepath: path + filename of desired text file to count words from
        :param min_wordsize: minimum number of letters in words to count (default is 1)
        :param max_results: returns this many items (default is 10)
        :param encoding: uses a specified encoding when reading from the file (default is utf-8-sig)
        :return: list of tuples containing words and count occurrences [(word, count), ...]
    """
    word_dict = defaultdict(int)

    with open(filepath, encoding=encoding) as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = re.sub(r'[.,!:?\';]', '', word.lower())   # This comes from a later chapter.
                if len(word) >= min_wordsize:
                    word_dict[word] += 1

    sorted_dict_items = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_dict_items[:max_results]


if __name__ == '__main__':
    sample_file = '../resources/gettysburg.txt'
    results = []
    try:
        results = word_counter(sample_file, min_wordsize=3, max_results=50)
        print(results)
    except IOError as err:
        print(f'Error working with file: {err}', file=sys.stderr)
    except UnicodeDecodeError as err:
        print(f'Unrecognized encoding: {err}', file=sys.stderr)
