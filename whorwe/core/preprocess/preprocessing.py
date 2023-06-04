
from konlpy.tag import Okt
from utils.read_data import data_read
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
    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    chat_data = make_morpheme(chat_data)
    words = words_counts(chat_data)
    active = active_time(chat_data)
    chat_data.to_csv('morph.csv', index=False)
    print('done')
