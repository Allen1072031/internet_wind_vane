# import logging
import requests
# import string
import jieba.analyse

from api import variable


def get_data():
    data = requests.get(f"https://newsapi.org/v2/top-headlines?"
                        f"country=tw&"
                        f"apiKey=53c8a63671e440029d766f5da8cbd487&"
                        f"pageSize=100").json()

    words = []
    for item in data['articles']:
        if item["description"]:
            word_list = jieba.analyse.extract_tags(item["title"]) + jieba.analyse.extract_tags(item["description"])
        else:
            word_list = jieba.analyse.extract_tags(item["title"])
        words += word_list

    variable.crawl_processing = variable.crawl_end

    return words


