
from konlpy.tag import Okt
import pandas as pd


def _tokenizer(data:pd.DataFrame):
    okt = Okt()
    data['new_content']= okt.pos(data['content'])

    return data


def remove_stopword(x):
    print('')


