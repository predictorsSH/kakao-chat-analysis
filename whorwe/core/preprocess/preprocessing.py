from konlpy.tag import Okt
from whorwe.core.functions.basic_analysis import words_counts, active_time
import pandas as pd


def _tokenizer(message: str):
    clean_words = []
    word_pos = []
    okt = Okt()
    morpheme = okt.pos(message)
    for word in morpheme:
        clean_words.append(word[0])
        word_pos.append(word[1])
    return clean_words, word_pos


def make_morpheme(data):
    data[['morpheme', 'pos']] = data['Message'].apply(lambda x: pd.Series(_tokenizer(x)))
    return data


def remove_stopword(x):
    print('')


if __name__ == '__main__':
    FILE_PATH = '../../../media/uploads/chat.txt'
    from utils.read_data import txt_read
    chat_data = txt_read(FILE_PATH)
    chat_data.to_csv('check.csv', index=False)
    chat_data = make_morpheme(chat_data)
    print('done')
    words = words_counts(chat_data)
    print('done')
    active = active_time(chat_data)
    print('done')

    # chat_data.to_csv('morph.csv', index=False)
    # print('done')
