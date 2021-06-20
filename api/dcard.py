import requests
import string
import jieba.analyse


def get_data():
    data = requests.get("https://www.dcard.tw/service/api/v2/posts?popular=true&limit=100").json()

    words = []
    for item in data:
        word_list = jieba.analyse.extract_tags(item["title"])
        for i in word_list:
            # if len(i) >= 2 and \
            #         i[0] not in string.ascii_letters and \
            #         i[0] not in string.digits and \
            #         i[0] not in string.punctuation:
            words.append(i)

    return words


