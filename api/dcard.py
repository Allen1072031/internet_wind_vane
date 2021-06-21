from api import variable

import logging
import requests
import jieba.analyse


def get_data(data_from="all", forum=""):
    if data_from == "all":
        if forum != "":
            logging.warning("forum does not use in 'all'")

        data = requests.get("https://www.dcard.tw/service/api/v2/posts?popular=true&limit=100").json()
        words = []
        for item in data:
            word_list = jieba.analyse.extract_tags(item["title"])
            words += word_list

        variable.crawl_processing = variable.crawl_end

        return words
    elif data_from == "forum":
        logging.info("forum")
        data = requests.get(f"https://www.dcard.tw/service/api/v2/forums/{forum}/posts?limit=100").json()
        words = []
        for item in data:
            word_list = jieba.analyse.extract_tags(item["title"]) + jieba.analyse.extract_tags(item["excerpt"])
            words += word_list

        variable.crawl_processing = variable.crawl_end

        return words

    return None
