import os
import json
import time
current_path = "D:\\LRFlashCardWord"  # 현재 작업 디렉토리를 가져옴
dListPath = "dramaList.json"
def get_file_list(path):
    file_list = []
    for file in os.listdir(path):
        if "RL_" not in file and file.endswith('.json'):
            file_list.append(file)
    return file_list


files = get_file_list(current_path)

dramaList = {}
dramaDetail = {}
for text in files:
    start_pattern = "wordlist_"
    end_pattern = ".WEBRip"
    start_index = text.find(start_pattern) + len(start_pattern)
    end_index = text.find(end_pattern)

    dramaName =text[start_index:end_index].rsplit('E', 1)[0]
    if "RL_"+dramaName not in dramaList and "wordlist_" in dramaList:
        count = 0
        saved_t =-1
        for file_name in files:
            if dramaName in file_name and 'ko' in file_name:
                count += 1
                t = os.path.getmtime(text)

                if saved_t < t:
                    saved_t = t
        dramaList["RL_"+dramaName]={"count":count,"time":time.ctime(saved_t)}

    if dramaName not in dramaDetail:
        dramaDetail[dramaName] = []
    if text[start_index:end_index] not in dramaDetail[dramaName]:
        dramaDetail[dramaName].append(text[start_index:end_index])
    # 파일 저장
    with open(current_path+'\\'+"RL_"+dListPath, 'w') as json_file:
        json.dump(dramaList, json_file)
    for dd in dramaDetail:
        with open(current_path + '\\' + "RL_"+dd + '.json', 'w') as json_file:
            json.dump(dramaDetail[dd], json_file)


print('writing list json completed ')