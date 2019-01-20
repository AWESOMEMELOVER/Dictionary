import fileinput
import re
import Serialization as save


regex = re.compile('[^a-zA-Z]')


def create_dictionary(*args):
    result_dict = {}

    def read_file():

        result_set = set()

        with fileinput.input(files=args[0]) as my_file:
            for line in my_file:
                for word in line.split():
                    result_set.add((regex.sub('', word.lower()), my_file.filename()))
        return sorted(result_set)

    set_of_tuples = read_file()

    for k, v in set_of_tuples:
        if k not in result_dict:
            result_dict[k] = [v]
        else:
            result_dict[k].append(v)

    return result_dict


if __name__ == '__main__':

   print(create_dictionary(('trash\\alice29.txt', 'trash\\asyoulik.txt', 'trash\\lcet10.txt', 'trash\\plrabn12.txt')))
