"""
    task4_1_starter.py

    In this task, you will modify the existing WordCounter class.
    Do this by:
    1) Converting the results() function into a read-only property
    2) Making min_wordsize a property
    3) Test the changes by providing a min_wordsize of 0.

    Refer to the course manual, following the pattern described to create
    the desired properties for this task.

"""
from collections import defaultdict


class WordCounter:
    def __init__(self, filepath, min_wordsize=1, max_results=10, encoding='utf-8'):
        self.word_dict = defaultdict(int)
        self.filepath = filepath
        self.min_wordsize = min_wordsize
        self.max_results = max_results
        self.encoding = encoding

    # Step 1. Add a property decorator here
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

    # Step 2. Add a min_wordsize getter (decorator + getter function)

    # Step 3. Add a min_wordsize setter (decorator + setter function)
    #         Ensure that min_wordsize can't be less than 1.  That's it--test it out!

sample_file = '../resources/gettysburg.txt'
counter = WordCounter(sample_file, min_wordsize=5)
print(counter.results(), counter.word_dict)
