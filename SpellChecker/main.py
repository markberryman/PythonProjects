import spellChecker
import time


file = open("dictionary.txt", 'r')

word_list = set()

for word in file:
    word = word.rstrip()    # trim newline
    word_list.add(word)

file.close()

while (True):
    word_to_check = input("> ")
    start_time = time.time()
    recommendation = spellChecker.SpellChecker.recommend(word_to_check, word_list)
    end_time = time.time()
    print(recommendation)
    print("Took {} seconds.".format(end_time - start_time))
