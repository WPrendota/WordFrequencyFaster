# Class with simple operations on text document words.

import re


class OperationsOnWordsInDocument:
    # Constructor requires file name/path, file encoding (utf8).
    def __init__(self, file_name, file_encoding):
        self.file_name = file_name
        self.file_encoding = file_encoding

    # File existance checker.
    def is_file_exist(self):
        try:
            file_txt = open(self.file_name, encoding=self.file_encoding)
            return True
        except FileNotFoundError:
            print(FileNotFoundError)

            return False

    # Word list checker.
    def word_find(self, check_word, word_list):

        for word_x in word_list:
            if word_x == check_word:
                return True

        return False

    # Word frequency counter.
    def word_frequency(self, words_len, count):
        word_f = count / words_len

        return word_f

    # Word counter and their frequency counter.
    def file_frequency_word(self):

        word_count_dictionary = {}

        update_word_number = 0
        update_word_frequency = 0

        if self.is_file_exist():
            file_txt = open(self.file_name, encoding=self.file_encoding)

            file_word_count = self.file_word_counter()

            while file_txt.readline():
                file_line = file_txt.readline()
                file_line = file_line.split(" ")
                word = file_line[0]

                if self.word_find(word, file_line):
                    if word in word_count_dictionary:
                        update_word_number = word_count_dictionary[word][0]
                        update_word_frequency = self.word_frequency(file_word_count, update_word_number + 1)
                        word_count_dictionary[word] = update_word_number + 1, update_word_frequency
                        del file_line[0]
                    else:
                        update_word_frequency = self.word_frequency(file_word_count, 1)
                        word_count_dictionary[word] = 1, update_word_frequency
                        del file_line[0]
        else:
            exit(-1)

        return word_count_dictionary

    # Text cleaner from characters without: "^A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż".
    def file_word_cleaner(self, text):
        return re.sub('[^A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', text)

    # Word counter.
    def file_word_counter(self):
        word_counter = 0

        if self.is_file_exist():
            with open(self.file_name, encoding=self.file_encoding) as file:
                while file.readline():
                    words_in_line = file.readline().replace("\n", " ")
                    words_in_line = self.file_word_cleaner(words_in_line)
                    words_in_line = words_in_line.split(' ')
                    word_counter += len(words_in_line)

            file.close()

        return word_counter