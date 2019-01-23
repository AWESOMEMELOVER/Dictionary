from Reader import Reader
from Parser import Parser
from Serializer import Serializer

if __name__ == '__main__':
    reader = Reader(
        ('trash\\alice29.txt',
         'trash\\asyoulik.txt',
         'trash\\lcet10.txt',
         'trash\\plrabn12.txt',
         'trash\\test.docx',
         'trash\\test3.docx',
         'trash\\shakespeer.txt',
         'trash\\BibleNIV.docx')
    )
    parser = Parser(reader)
    serializer = Serializer()

    my_dict = parser.create_dictionary()
    print(len(serializer.read_from_txt()))
