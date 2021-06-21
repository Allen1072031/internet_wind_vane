import jieba
import jieba.analyse

from api import dcard, news, ptt, variable

from wordcloud import WordCloud
# import matplotlib.pyplot as plt


file_path = __path__[0].replace("\\", "/")


def __init__():
    jieba.set_dictionary(file_path + "/res/dict.txt")
    jieba.load_userdict(file_path + "/res/user.txt")
    jieba.analyse.set_idf_path(file_path + "/res/idf.txt")
    jieba.analyse.set_stop_words(file_path + "/res/stop.txt")
    jieba.initialize()

    variable.progress_init()


def get_data(api: str, *args, **kwargs):
    # print(kwargs)
    if api == "dcard":
        if kwargs["data_from"] and kwargs["forum"]:
            return dcard.get_data(data_from=kwargs["data_from"], forum=kwargs["forum"])
        elif kwargs["data_from"]:
            return dcard.get_data(data_from=kwargs["data_from"])
        return dcard.get_data()
    elif api == "ptt":
        return ptt.get_data(ptt_id=kwargs["ptt_username"], password=kwargs["ptt_password"])
    elif api == "news":
        return news.get_data()

    return None


def gen_wordcloud(words):
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=file_path + "/font/SourceHanSansTW-Regular.otf"
    )
    wordcloud.generate(" ".join(words))

    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()

    wordcloud.to_file("image/cloud.png")



