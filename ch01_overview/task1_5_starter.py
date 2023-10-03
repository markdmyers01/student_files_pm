"""

      task1_5_starter.py   -

      This solution attempts to read from alice.txt and display the most
      frequent 100 words that are 5 characters or greater


      Follow these steps/tips:
      1. Create an empty dictionary to store words and word counts

      2. Iterate over the file as shown in the slide for this task.

      3. Use the split() method to break one line into a list of strings

      4. Iterate over the list of strings, check if the word is in the
         dictionary already

         Hint: use   if word in wordcount:

      5. If it is, increment the count value for that word

         Hint: use   wordcount[word] += 1

      6. If it is not, add it to the dictionary

         Hint:  use
                   else:
                       wordcount[word] = 1

         That's it for building the dictionary.  Now it's time to sort it.

      7. To sort the dictionary, convert it to a list of tuples using dict.items()
         and pass this into sorted()

      8. To sort based on the values, we'll need a key= function. We
         need to sort by the values, in other words, the second item in the tuple.
         The following should do this:
                     key = lambda a: a[1]

      9. Sort using sorted(list, key, order)   <-- plug step 7 and step 8 into this and set the reverse flag

         Hint:   sorted(wordcount.items(), key=lambda a: a[1], reverse=True)

      10. sorted() returns a new list of tuples in sorted order.   Iterate over this new
          list and create a list of only the words that are 5 characters or longer.
          You can do this with a for loop, but can you do it with a list comprehension?

          Hint:  [pair for pair in sortedwords if len(pair[0) >= 5]

      11. Print the first 100 of the items in this new list.

          Hint: use slicing to limit the output
"""
wordcount = {}

for line in open('alice.txt', encoding='utf-8-sig'):
    words = line.split()
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

print([item for idx, item in enumerate(wordcount.items()) if idx < 5 ])

for idx, item in enumerate(wordcount.items()):
    print(item)
    if idx == 4:
        break


sortedwords = sorted(wordcount.items(), key=lambda a : a[1], reverse=True)
print(sortedwords[: 5])


five_letters = [(word, count) for word, count in sortedwords if len(word) >= 5]

print(five_letters[:100])