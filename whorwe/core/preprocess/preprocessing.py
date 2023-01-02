
from konlpy.tag import Okt
from whorwe.core.functions.read_data import data_read
from whorwe.core.functions.basic_analysis import words_counts, active_time

def _tokenizer(message: str):
    clean_words=[]
    okt = Okt()
    morpheme = okt.pos(message)
    for word in morpheme:
        if word[1] not in ['Josa', 'Eomi', 'Punctuation', 'Determiner',
                           'Adjective', 'Modifier', 'Number', 'Suffix',
                           'VerbPrefix', 'PreEomi']:
            clean_words.append(word[0])
    return clean_words

def make_morpheme(data):
    data['morpheme'] = data['Message'].apply(_tokenizer)
    return data

def remove_stopword(x):
    print('')

if __name__ == '__main__':
    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    chat_data = make_morpheme(chat_data)
    words = words_counts('징옆', chat_data)
    active = active_time(chat_data)



