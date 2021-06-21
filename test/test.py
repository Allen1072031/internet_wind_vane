import requests
import jieba
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt


if __name__ == '__main__':
    text = requests.get("https://www.dcard.tw/service/api/v2/posts?popular=true&limit=100").json()

    # for i in text[0].keys():
    #     print(i)

    words = []
    for item in text:
        word_list = jieba.cut(item["title"])
        for i in word_list:
            if len(i) >= 2 and i[0] not in string.ascii_letters and i[0] not in string.digits and i[0] not in string.punctuation:
                words.append(i)
    print(words)

    # for i in range(len(words)):
    #     words[i] = words[i].encode("big5")

    my_wordcloud = WordCloud(background_color='white', font_path="../api/font/SourceHanSansTW-Regular.otf")
    img = my_wordcloud.generate(" ".join(words))

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

    my_wordcloud.to_file("cloud.png")
