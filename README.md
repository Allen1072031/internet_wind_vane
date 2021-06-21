# 網路風向儀 internet_wind_vane

## Introduction
在網路論壇，每天有數以萬計的文章產生，但是大量的文章數難以閱讀，以人力分析是一件費時費力的工作。
而在大量的文字中，會有許多重複的語詞，將語助詞(例如，哇、喔)、連結詞(例如，和、還有)去除之後，剩下的名詞、動詞等，大致上可以稱為關鍵字。
關鍵字出現頻率越高，越有可能是當前的熱門話題。

本程式將會使用API去抓取資料，分別使用PyPTT、Dcard API，以及NEWS API，去抓取在PTT、Dcard，以及台灣新聞的內容。
並且使用jieba處裡中文分詞問題，還有除去非必要的語助詞、連結詞。
GUI介面是使用tkinter來建立，再使用word cloud(文字雲)來視覺化呈現關鍵詞的熱門度

## Build Process
### Required Packages Installation
```shell
pip3 install -r requirements.txt
```
file: [requirements.txt](requirements.txt)

### Execute
```shell
python3 internet_wind_vane.py
```

## Detail
### Project Structure
```
.
├── README.md
├── api
│   ├── __init__.py
│   ├── dcard.py
│   ├── font
│   │   └── SourceHanSansTW-Regular.otf
│   ├── news.py
│   ├── ptt.py
│   ├── res
│   │   ├── dict.txt  -> For jieba default dictionary
│   │   ├── idf.txt   -> For jieba TF-IDF Algorithm
│   │   ├── stop.txt  -> For jieba stop word (不出現的字詞、符號)
│   │   └── user.txt  -> For jieba user-defined dictionary
│   └── variable.py
├── image
│   └── cloud.png -> word cloud image
├── internet_wind_vane.py -> main enter
├── requirements.txt
├── test
└── window.py -> GUI
```
### Dcard API

### NEWS API

### PyPtt

## Result
![image]()

## Reference
1. [PyPtt](https://github.com/PttCodingMan/PyPtt)
2. [jieba](https://github.com/fxsjy/jieba)
3. [Dcard API](https://blog.jiatool.com/posts/dcard_api_v2/)
4. [NEWS API](https://newsapi.org/)
5. [WordCloud](https://amueller.github.io/word_cloud)
6. [tkinter document](https://tkdocs.com/)
