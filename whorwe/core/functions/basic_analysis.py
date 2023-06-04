import pandas as pd


# 사용자
def user(data) -> list:
    users = data['User'].unique()
    return users


# 말 많은 사람 찾기
def user_counts(data):
    u_counts = data['User'].value_counts()
    return u_counts


def words_counts(data, pos='Noun'):

    data = data[['morpheme', 'pos']]
    counts = dict()

    for d_i, d in enumerate(data['morpheme']):
        for w_i, word in enumerate(d):
            if data.iloc[d_i]['pos'][w_i] == pos:
                counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(),  key=lambda x: x[1], reverse=True)


def all_user_word(data):
    print('counting words by all users...')

    all_words_counts = []
    w_counts = words_counts(data, pos='Noun')
    cnt = 0
    len_2 = 0

    for w in w_counts:
        if cnt > 150:
            break

        elif len(w[0]) == 1:
            continue

        elif len_2 < 30:
            if ('사진' != (w[0])) & ('이모티콘' != (w[0])):
                all_words_counts.append(w)
                cnt += 1
                if len(w[0]) == 2:
                    len_2 += 1

        else:
            if len(w[0]) == 2:
                continue
            else:
                if ('사진' != (w[0])) & ('이모티콘' != (w[0])):
                    all_words_counts.append(w)
                    cnt += 1

    return all_words_counts


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
    from utils.read_data import data_read

    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    u_counts = user_counts(chat_data)

    # act_time = active_time(chat_data)
