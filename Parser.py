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

    def __get_index_by_filename(self, filename):
        return self.my_filenames.index(filename)

    def __get_boolean_by_filename(self, filename):
        result = []
        list_of_all_files = [item for item in self.my_filenames]
        for item in list_of_all_files:
            if item in filename:
                result.append(1)
            else:
                result.append(0)
        return result

    def create_inverted_index(self):
        result_dict = {}

        for k, v in self.my_tuples:
            if k not in result_dict:
                result_dict[k] = [self.__get_index_by_filename(v)]
            else:
                result_dict[k].append(self.__get_index_by_filename(v))
        return result_dict

    def create_incident_matrix(self):
        it = itertools.groupby(self.my_tuples, lambda x: x[0])
        for key, subiter in it:
            yield key, sum(item[1] for item in subiter)

    """    def create_dictionary(self):
        result_dict = {}
        set_of_tuples = self.__fetch_tuples()

        for k, v in set_of_tuples:
            if k not in result_dict:
                result_dict[k] = [v]
            else:
                result_dict[k].append(v)
        return result_dict

    def create_incident_matrix(self):

        copied_dictionary = self.my_dictionary.copy()

        list_of_all_files = [item for item in reader.my_args[0]]

        def convert_list_to_matrix(list_of_presents_files):
            result = []
            for item in list_of_all_files:
                if item in list_of_presents_files:
                    result.append(1)
                else:
                    result.append(0)
            return result

        for key in copied_dictionary:
            copied_dictionary[key] = convert_list_to_matrix(copied_dictionary[key])

        return copied_dictionary
"""


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
    print(list(parser.create_incident_matrix()))



