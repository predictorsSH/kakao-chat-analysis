import pandas as pd

FILE_PATH = '../../media/uploads/KakaoTalk_Chat.csv'


def data_read(file_path):
    chat_data = pd.read_csv(file_path)
    print(chat_data.info())
    return chat_data


if __name__ == '__main__':
    chat_data = data_read(FILE_PATH)
    chat_data.head(3)