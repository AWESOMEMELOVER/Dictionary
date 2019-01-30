import re
import itertools
from Reader import Reader


class Parser:
    regex = re.compile('[^a-zA-Z]')

    def __init__(self, my_reader):
        self.reader = my_reader
        self.tuples_of_string = self.reader.get_files()
        self.my_tuples = self.__fetch_tuples()
        self.my_filenames = self.reader.my_args[0]

    def __fetch_tuples(self):
        result_set = set()

        for my_tuple in self.tuples_of_string:
            for word in my_tuple[1].split():
                result_set.add((self.regex.sub('', word.lower()), my_tuple[0]))

        return sorted(result_set)

    def create_inverted_index(self):
        result_dict = {}

        for k, v in self.my_tuples:
            if k not in result_dict:
                result_dict[k] = [self.my_filenames.index(v)]
            else:
                result_dict[k].append(self.my_filenames.index(v))
        return result_dict

    def create_incident_matrix(self):
        result_dict = {}

        it = itertools.groupby(self.my_tuples, lambda x: x[0])
        for key, subiter in it:
            # key, [item for item in subiter[1]]
            list_of_present_files = [item[1] for item in subiter]
            result_dict[key] = [1 if element in list_of_present_files else 0 for element in self.my_filenames]
        return result_dict


if __name__ == '__main__':
    reader = Reader(
        ('trash\\alice29.txt',
         'trash\\asyoulik.txt',
         'trash\\lcet10.txt',
         'trash\\plrabn12.txt',
         'trash\\test.docx',
         'trash\\BibleNIV.docx',
         'trash\\shakespeer.txt',
         'trash\\test.docx',
         'trash\\test3.docx')
    )
    parser = Parser(reader)
    print(parser.create_incident_matrix())



