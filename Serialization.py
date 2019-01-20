import pickle as pickle


def save_to_txt(dict):
    with open('dict.txt', mode='w') as file:
        file.write(str(dict))


def save_to_pickle(dict):
    with open('dict.pickle', mode='wb') as file:
        pickle.dump(dict, file)


def load_from_pick():
    with open('dict.pickle', 'rb') as file:
        data_new = pickle.load(file)
        return data_new
