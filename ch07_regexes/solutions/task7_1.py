"""

      task7_1.py   -

      This solution modifies the solution from task1_6.
      It attempts to read from alice.txt and display the most
      frequent 100 words that are 5 characters or greater but for
      this requirement it removes punctuation and capitalized words.

      The only line added to this solution is found on line 23 below.

"""
import re
import sys
wordcount = {}

try:
    with open('alice.txt', encoding='utf8') as f:
        for line in f:
            words = line.split()

            for word in words:
                word = re.sub(r'[.!\?,:"]','', word.lower())
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1
except IOError as err:
    print(err, file=sys.stderr)
    sys.exit()

sortedwords = sorted(wordcount.items(), key=lambda a:a[1], reverse=True)
five_letters = [(word, count) for word, count in sortedwords if len(word) >= 5]
print(five_letters[:100])
