import fileinput
import re
<<<<<<< HEAD
import Serialization as save

=======
>>>>>>> 94e1d1fb3b587d6f26b01bf86da532798087b469

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

    print(create_dictionary(('alice29.txt', 'asyoulik.txt', 'lcet10.txt', 'plrabn12.txt')))

