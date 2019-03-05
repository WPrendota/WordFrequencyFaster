# Class with simple operations on text document lines.

class OperationsOnLinesInDocument:
    # Constructor requires file name/path and file encoding (utf8).
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

    # Line counter.
    def file_line_counter(self):
        line_counter = 0

        if self.is_file_exist():
            with open(self.file_name, encoding=self.file_encoding) as file:
                for line in file:
                    line_counter += 1

            file.close()
        return line_counter