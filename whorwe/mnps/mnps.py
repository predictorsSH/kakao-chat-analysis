from whorwe.core.preprocess.preprocessing import make_morpheme
from whorwe.core.functions.read_data import data_read
from whorwe.core.functions.basic_analysis import words_counts, active_time, user_counts, user


class DataProcess():
    def __init__(self, file_path):
        self.file_path = file_path
        self.chat_data = data_read(self.file_path)
        self.users = user(self.chat_data)
        self.none_count_if_include = ['ㅋ', 'ㅎㅎ', 'ㅇㅇ']
        self.none_count_words = ['\n', '사진', '이모티콘']
    def preprocess(self):
        return make_morpheme(self.chat_data)

    def basic_analysis(self):

        analysis_data = self.preprocess()
        u_count = user_counts(analysis_data)  # 등장 횟수 카운트
        act_time = active_time(analysis_data)  # 대화가 가장 활발한 시간
        w_counts = self.all_user_word(analysis_data)

        return u_count, act_time, w_counts

    def all_user_word(self, data):
        all_words_counts = []
        w_counts = words_counts('ALL',data)


        for w in w_counts:
            if (len(w[0]) == 2) & ('사진' != (w[0])):
                all_words_counts.append(w) #순위 높은 단어 10개만 우선
            if len(all_words_counts) == 30:
                break

        for w in w_counts:
            if (len(w[0]) >= 3) & ('이모티콘' != (w[0])):
                all_words_counts.append(w)
            if len(all_words_counts) == 120:
                break

        return all_words_counts

    def user_word(self, data):
        u_words_counts = []
        for u in self.users:
            word_list = []
            w_counts = words_counts(u, data)

            for w in w_counts:

                if (len(w[0]) >= 3) & ('사진' != (w[0])) & ('이모티콘' != (w[0])):
                    word_list.append(w) #순위 높은 단어 10개만 우선
                if len(word_list) >= 10:
                    break

            u_words_counts.append({u: word_list})
        return u_words_counts




if __name__=='__main__':

    FILE_PATH = '../../media/uploads/KakaoTalk_Chat_코따까리들_2023-04-25-21-34-56.csv'
    DP = DataProcess(FILE_PATH)
    u_count, act_time, u_words_counts = DP.basic_analysis()
