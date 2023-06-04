from whorwe.core.preprocess.preprocessing import make_morpheme
from utils.read_data import data_read
from whorwe.core.functions.basic_analysis import active_time, user_counts, user, all_user_word


class DataProcess:
    def __init__(self, file_path):
        self.file_path = file_path
        self.chat_data = data_read(self.file_path)
        self.users = user(self.chat_data)

    def preprocess(self):
        return make_morpheme(self.chat_data)

    def basic_analysis(self):
        analysis_data = self.preprocess()
        u_count = user_counts(analysis_data)  # 등장 횟수 카운트
        act_time = active_time(analysis_data)  # 대화가 가장 활발한 시간
        w_counts = all_user_word(analysis_data)

        return u_count, act_time, w_counts


if __name__ == '__main__':

    FILE_PATH = '../../media/uploads/KakaoTalk_Chat.csv'
    DP = DataProcess(FILE_PATH)
    u_count, act_time, u_words_counts = DP.basic_analysis()
    u_words_counts