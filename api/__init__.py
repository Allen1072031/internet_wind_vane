import jieba
import jieba.analyse

from api import dcard

from wordcloud import WordCloud
import matplotlib.pyplot as plt


file_path = __path__[0].replace("\\", "/")
jieba.set_dictionary(file_path + "/res/dict.txt")
jieba.analyse.set_idf_path(file_path + "/res/idf.txt")
jieba.analyse.set_stop_words(file_path + "/res/stop.txt")
jieba.initialize()


def get_data(api, *args):
    if api == "dcard":
        return dcard.get_data()
    elif api == "ptt":
        pass
    elif api == "news":
        pass

    return None


def gen_wordcloud(words):
    wordcloud = WordCloud(background_color='white',
                          font_path=file_path + "/font/SourceHanSansTW-Regular.otf")
    wordcloud.generate(" ".join(words))

    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()

    wordcloud.to_file("image/cloud.png")



