from preprocessing import make_morpheme
from read_data import data_read
from basic_analysis import words_counts, active_time, user_counts, user


class DataProcess():
    def __init__(self, file_path):
        self.file_path = file_path
        self.chat_data = data_read(self.file_path)
        self.users = user(self.chat_data)

    def preprocess(self):
        return make_morpheme(self.chat_data)

    def basic_analysis(self):

        analysis_data = self.preprocess()
        u_count = user_counts(analysis_data)

        words_counts_lst = []
        for u in self.users:
            w_counts = words_counts(u, analysis_data)
            words_counts_lst.append(w_counts[:10]) #순위 높은 단어 10개만 우선
        act_time = active_time(analysis_data) #??

        return u_count, words_counts_lst, act_time



if __name__=='__main__':

    FILE_PATH = '../../media/uploads/KakaoTalk_Chat.csv'
    DP = DataProcess(FILE_PATH)
    u_count, words_counts, active_time = DP.basic_analysis()
