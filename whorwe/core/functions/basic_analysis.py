import pandas as pd


# 사용자
def user(data) -> list:
    users = data['User'].unique()
    return users


# 말 많은 사람 찾기
def user_counts(data):
    u_counts = data['User'].value_counts()
    return u_counts


def words_counts(data):

    data = data[['morpheme', 'pos']]
    counts = {}
    print('counting words by all users...')
    for d_i, d in enumerate(data['morpheme']):
        for w_i, word in enumerate(d):
            if data.iloc[d_i]['pos'][w_i] == 'Noun':
                counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(),  key=lambda x: x[1], reverse=True)


def active_time(data):

    time = [i for i in range(1, 25)]
    time_df = pd.DataFrame(index=time)

    data['Date'] = pd.to_datetime(data['Date'])
    data['hour'] = data['Date'].dt.hour
    result = data[['hour', 'Message']].groupby(by=['hour']).count()

    time_df = time_df.join(result).fillna(0).astype(int)['Message']
    time_count_dict = {}
    for t, v in time_df.items():
        time_count_dict[t] = v
    return time_count_dict


if __name__ == '__main__':
    from whorwe.core.functions.read_data import data_read

    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    # chat_data = data_read(FILE_PATH)
    # u_counts = user_counts(chat_data)
    # act_time = active_time(chat_data)
