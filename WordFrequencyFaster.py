# Faster version:

import sys
import re
import time


def word_find(check_word, word_list):

    for word_x in word_list:
        if word_x == check_word:
            return True

    return False


def word_frequency(words_len, count):
    word_f = count/words_len

    return word_f


def file_word_counter(file_name):
    word_counter = 0

    with open(file_name, encoding="utf8") as file:
        while file.readline():
            words_in_line = file.readline().replace("\n", " ")
            words_in_line = re.sub('[^A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', words_in_line)
            words_in_line = words_in_line.split(' ')
            word_counter += len(words_in_line)

    file.close()

    return word_counter


def is_file_exist(file_name):
    try:
        file_txt = open(file_name, encoding="utf8")
        return True
    except FileNotFoundError:
        print(FileNotFoundError)

        return False


def not_end_of_file(current_line_number, total_line_number):

    if current_line_number == total_line_number:
        return False
    else:
        return True


def file_line_counter(file_name):
    line_counter = 0

    with open(file_name, encoding="utf8") as file:
        for line in file:
            line_counter += 1

    file.close()
    return line_counter


def word_frequency_faster(file_name, file_encoding):
    start_time = time.time()

    word_count_dictionary = {}

    update_word_number = 0
    update_word_frequency = 0

    if is_file_exist(file_name):
        file_txt = open(file_name, encoding=file_encoding)

        file_exist = is_file_exist(file_name)
        file_word_count = file_word_counter(file_name)
        file_line_count = file_line_counter(file_name)

        word_list = []

        while file_txt.readline():
            file_line = file_txt.readline()
            file_line = file_line.split(" ")
            word = file_line[0]

            if word_find(word, file_line):
                if word in word_count_dictionary:
                    update_word_number = word_count_dictionary[word][0]
                    update_word_frequency = word_frequency(file_word_count, update_word_number + 1)
                    word_count_dictionary[word] = update_word_number + 1, update_word_frequency
                    del file_line[0]
                else:
                    update_word_frequency = word_frequency(file_word_count, 1)
                    word_count_dictionary[word] = 1, update_word_frequency
                    del file_line[0]
    else:
        exit(-1)

    print(word_count_dictionary)

    elapsed_time = time.time() - start_time

    print(elapsed_time)


if __name__ == "__main__":
    word_frequency_faster(sys.argv[1], sys.argv[2])