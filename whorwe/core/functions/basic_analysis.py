from read_data import data_read

def user_counts(data):
    u_counts = data['User'].value_counts()
    return u_counts


if __name__ =='__main__':
    FILE_PATH = '../../../media/uploads/KakaoTalk_Chat.csv'
    chat_data = data_read(FILE_PATH)
    u_counts = user_counts(chat_data)
