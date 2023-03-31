from whorwe.core.preprocess.preprocessing import make_morpheme
from whorwe.core.functions.read_data import data_read
from whorwe.core.functions.basic_analysis import words_counts, active_time, user_counts, user


class DataProcess():
    def __init__(self, file_path):
        self.file_path = file_path
        self.chat_data = data_read(self.file_path)
        self.users = user(self.chat_data)

    def preprocess(self):
        return make_morpheme(self.chat_data)

    def basic_analysis(self):

        analysis_data = self.preprocess()
        u_count = user_counts(analysis_data)  #등장 횟수 카운트
        act_time = active_time(analysis_data) #대화가 가장 활발한 시간
        w_counts = self.all_user_word(analysis_data)

        return u_count, act_time, w_counts

    def all_user_word(self, data):
        u_words_counts = []
        for u in self.users:
            word_list = []
            w_counts = words_counts(u, data)


            for w in w_counts:

                if ('ㅋ' not in (w[0])) and ('\n' != w[0]) & (len(w[0]) >= 3) \
                        & ('ㅇㅇ' not in (w[0])) & ('사진' != (w[0])) & ('이모티콘' != (w[0])):
                    word_list.append(w) #순위 높은 단어 5개만 우선
                if len(word_list) >= 10:
                    break

            u_words_counts.append({u: word_list})
        return u_words_counts


if __name__=='__main__':

    FILE_PATH = '../../media/uploads/KakaoTalk_Chat_LhVd00Y_C4XecUs.csv'
    DP = DataProcess(FILE_PATH)
    u_count, act_time, u_words_counts = DP.basic_analysis()
