
from konlpy.tag import Okt
from read_data import data_read
from basic_analysis import words_counts

def _tokenizer(message: str):
    okt = Okt()
    morpheme = okt.pos(message)
    return morpheme

def make_morpheme(data):
    data['morpheme'] = data['Message'].apply(_tokenizer)
    return data

def remove_stopword(x):
    print('')

if __name__ == '__main__':
    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    chat_data = make_morpheme(chat_data)
    words = words_counts('김상현',chat_data)



