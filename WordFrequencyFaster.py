import time
from argparse import ArgumentParser
from OperationsOnLinesInDocument import OperationsOnLinesInDocument
from OperationsOnWordsInDocument import OperationsOnWordsInDocument

# Main function
def main(args):
    if args.w:
        if args.p:
            oow = OperationsOnWordsInDocument(args.w, 'utf8')
            for word in oow.file_frequency_word():
                print(word)

        if args.c:
            oow = OperationsOnWordsInDocument(args.w, 'utf8')
            print(oow.file_frequency_word())

        if not args.c and not args.p:
            oow = OperationsOnWordsInDocument(args.w, 'utf8')
            print(oow.file_word_counter())
    if args.l:
            ool = OperationsOnLinesInDocument(args.l, "utf8")
            print(ool.file_line_counter())

# Argument Parser:
def arg_pars():
    parser = ArgumentParser(description='Text document finder.')
    parser.add_argument('-w', type=str,
                        help='Print number of all words from a text document with utf8 encoding. Usage: [-w][file_name]')
    parser.add_argument('-p', action='store_true',
                        help='Print all words from word searcher. Usage: [-w][file_name][-p]')
    parser.add_argument('-c', action='store_true',
                        help='Print all words with frequency from word searcher. Usage: [-w][file_name][-c]')
    parser.add_argument('-l',
                        help='Print number of all lines from a text document with utf8 encoding. Usage: [-l][file_name]')

    return parser.parse_args()


if __name__ == "__main__":
    start_time = time.time()

    main(arg_pars())    #Parsed arguments are moved to main function.

    elapsed_time = time.time() - start_time

    print(elapsed_time) #Printing time of program running.