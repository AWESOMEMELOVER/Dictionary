import fileinput
import re


def parse_file(path):
        regex = re.compile('[^a-zA-Z]')

        doc_id = path.split('\\')[-1]

        def read_file(path):
            with open(path, 'r') as my_file:
                return my_file.read()

        return sorted(set((regex.sub('', letter.lower()), doc_id) for (index, letter) in enumerate(read_file(path).split())))


def test_func():
    with fileinput.input(files=('C:\\Users\\micka\\tplink.txt', 'C:\\Users\\micka\\tplink2.txt')) as my_file:
        pass


if __name__ == '__main__':
    test_func()
