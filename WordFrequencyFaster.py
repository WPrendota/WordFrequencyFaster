# Faster version:

import re
import time

#-------------------------------------------------------------

start_time = time.time()

#-------------------------------------------------------------

text = open(r"C:\Users\Witek\Desktop\pan-tadeusz.txt", encoding="utf8").read()
words = text.replace("\n", " ")
words = re.sub('[^A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', words)
words = words.split(' ')

#-------------------------------------------------------------

wor = []

def word_find_new(check_word, word_list):

    for x_word in word_list:
        if x_word == check_word:
            return True

    return False

#-------------------------------------------------------------

def word_frequency(words_len, count):
    word_f = count/words_len

    return word_f

#-------------------------------------------------------------

count_list = {}

update_v = 0
update_f = 0
words_l = words.__len__()

while(words):
    word = words[0]

    if word_find_new(word, words):
        if word in count_list:
            update_v = count_list[word].__getitem__(0)

            update_f = word_frequency(words_l, update_v+1)

            count_list[word] = update_v+1, update_f

            del words[0]
        else:
            update_f = word_frequency(words_l, 1)
            count_list[word] = 1, update_f
            del words[0]

print(count_list)

#-------------------------------------------------------------

elapsed_time = time.time() - start_time

print(elapsed_time)