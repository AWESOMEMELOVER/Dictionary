import re
from Reader import Reader


class Parser:
    regex = re.compile('[^a-zA-Z]')

    def __init__(self, my_reader):
        self.tuples_of_string = my_reader.get_files()

    def __fetch_tuples(self):
        result_set = set()

        for my_tuple in self.tuples_of_string:
            for word in my_tuple[1].split():
                result_set.add((self.regex.sub('', word.lower()), my_tuple[0]))

        return sorted(result_set)

    def create_dictionary(self):
        result_dict = {}
        set_of_tuples = self.__fetch_tuples()

        for k, v in set_of_tuples:
            if k not in result_dict:
                result_dict[k] = [v]
            else:
                result_dict[k].append(v)
        return result_dict


if __name__ == '__main__':
    reader = Reader(
        ('trash\\alice29.txt', 'trash\\asyoulik.txt', 'trash\\lcet10.txt', 'trash\\plrabn12.txt', 'trash\\test.docx')
    )
    parser = Parser(reader)
    print(parser.create_dictionary())


