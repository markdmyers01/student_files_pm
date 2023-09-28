"""

      task7_1_starter.py   -

      This starter file is a repeat of the solution presented for
      task1_5.py.  This task required reading the entire book and counting
      the top 100 5-letter or more words found in the book.

      The new requirement is to use regular expressions to filter out
      punctuation and to ignore case when checking for the top 100 5-letter
      words found in the book.

      Step 1:
        Use re.sub() as described in the materials.  Use the following
        provided regular expression and make sure to convert keys to lower
        case using the string class' lower() method.

        r'[.!\?,:"]'

"""

wordcount = {}

for line in open('alice.txt', encoding='utf8'):
    words = line.split()

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

sortedwords = sorted(wordcount.items(), key=lambda a:a[1], reverse=True)
five_letters = [(word, count) for word, count in sortedwords if len(word) >= 5]
print(five_letters[:100])
