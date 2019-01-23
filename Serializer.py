import pickle as pickle
import ast

from Reader import Reader
from Parser import Parser


class Serializer:

    def save_to_txt(self, dictionary):
        with open('dict.txt', mode='w') as file:
            file.write(str(dictionary))

    def read_from_txt(self):
        with open('dict.txt', mode='r') as file:
            return ast.literal_eval(file.read())

    def save_to_pickle(self, dictionary):
        with open('dict.pickle', mode='wb') as file:
            pickle.dump(dictionary, file)

    def load_from_pick(self):
        with open('dict.pickle', 'rb') as file:
            data_new = pickle.load(file)
            return data_new


if __name__ == '__main__':
    reader = Reader(
        ('trash\\alice29.txt', 'trash\\asyoulik.txt', 'trash\\lcet10.txt', 'trash\\plrabn12.txt', 'trash\\test.docx')
    )
    parser = Parser(reader)
    my_dict = parser.create_dictionary()

    serializer = Serializer()

    print(serializer.load_from_pick())
