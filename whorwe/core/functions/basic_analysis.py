from whorwe.core.functions.read_data import data_read
import pandas as pd


# 사용자
def user(data) -> list:
    users = data['User'].unique()
    return users


# 말 많은 사람 찾기
def user_counts(data):
    u_counts = data['User'].value_counts()
    return u_counts


def words_counts(user, data):
    data = data[data['User'] == user]['morpheme']

    counts = {}
    print('counting words by ', user, '...')
    for d in data:
        for word in d:
            counts[word] = counts.get(word, 0) + 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)


def active_time(data, user=None):
    if user == None:
        data['Date'] = pd.to_datetime(data['Date'])
        data['hour'] = data['Date'].dt.hour
        return data[['hour', 'Message', 'User']].groupby(by=['User', 'hour']).count()

    else:
        data['Date'] = pd.to_datetime(data['Date'])
        data['hour'] = data['Date'].dt.hour
        return data[data['User'] == user][['hour', 'Message']].groupby(by=['hour']).count()


if __name__ == '__main__':
    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    u_counts = user_counts(chat_data)
