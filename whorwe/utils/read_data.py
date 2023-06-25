import pandas as pd
import re


def data_read(file_path):
    chat_data = pd.read_csv(file_path)
    print(chat_data.info())
    return chat_data


def txt_read(file_path):


    pattern = r'-----+ (\d+)년 (\d+)월 (\d+)일 [월화수목금토일]요일 ----+'
    chat_data = []

    with open(file_path, 'r') as f:
        f_data = f.readlines()
        match = re.fullmatch(pattern, f_data[3].strip())
        date = [match.group(1), match.group(2), match.group(3)]
        date = '-'.join(date)

        for line in f_data[4:]:
            line = line.strip()

            try:
                match = re.fullmatch(pattern, line)
            except re.error as e:
                print("정규식 오류로 스킵, e")

            if match:

                date = [match.group(1), match.group(2), match.group(3)]
                date = '-'.join(date)

            elif re.fullmatch(r'\[.+?] \[(오전|오후) \d{1,2}:\d{2}] .+?', line):

                try:
                    user_start = line.find("[") + 1
                    user_end = line.find("]")
                    user = line[user_start:user_end]

                    # 시간 추출
                    time_start = line.find("[", user_end + 1) + 1
                    time_end = line.find("]", time_start)
                    time = line[time_start:time_end]
                    period = time.split(' ')[0]
                    time = time.split(' ')[1]

                    if period == '오후' and time.split(':')[0] != '12':
                        time = [str(int(time.split(':')[0]) + 12), time.split(':')[1]]
                        time = ':'.join(time)

                    else:
                        time = time

                    # Message
                    message_start = line.find(" ", time_end + 1) + 1
                    message = line[message_start:]

                except:
                    continue
            chat_data.append({'Date': date + ' ' + time, 'User': user, 'Message': message})
    chat_data = pd.json_normalize(chat_data)
    return chat_data



if __name__ == '__main__':

    import os
    print(os.getcwd()) # 작업 위치 /Users/sanghyun/IdeaProjects/whoweare/whorwe/core/functions'

    FILE_PATH = '../../../media/uploads/chat.txt'
    txt_data = txt_read(FILE_PATH)
