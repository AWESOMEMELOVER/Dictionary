import docx2txt


class Reader:

    def __init__(self, *args):
        dict()
        self.my_args = args
        self.files = map(lambda x: open(x, 'r').read() if x.split('.')[1] == 'txt' else docx2txt.process(x), args[0])

    def get_files(self):
        result_list = []
        for index, string in enumerate(self.files):
            result_list.append((self.my_args[0][index], string))
        return result_list


if __name__ == '__main__':
    reader = Reader(
        ('trash\\alice29.txt', 'trash\\asyoulik.txt', 'trash\\lcet10.txt', 'trash\\plrabn12.txt', 'trash\\test.docx')
    )
    for file in reader.get_files():
        print(file)

