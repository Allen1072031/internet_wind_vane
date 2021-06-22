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
Dcard API使用GET來request，根據不同的參數可以獲得json的response。
主要是抓取熱門文章，和看版的文章，並取得title和excerpt的資訊。
#### Example
```curl
# 取得100份全部文章分類的熱門文章
GET https://www.dcard.tw/service/api/v2/posts?popular=true&limit=100

# 取得100份元智大學看板的文章
GET https://www.dcard.tw/service/api/v2/forums/yzu/posts?limit=100
```

```json
[
    {
        "id":236303953,
        "title":"標題",
        "excerpt":"摘要",
        "anonymousSchool":true,
        "anonymousDepartment":true,
        "pinned":false,
        "forumId":"42851318-b9e2-4a75-8a05-9fe180becefe",
        "replyId":236300230,
        "createdAt":"2021-06-21T02:13:40.449Z",
        "updatedAt":"2021-06-22T01:03:37.740Z",
        "commentCount":227,
        "likeCount":7314,
        "withNickname":false,
        "tags":["HIDE_THUMBNAIL"],
        "topics":["*","*","*","*","*"],
        "meta":{"layout":"classic"},
        "globalPinned":null,
        "forumName":"*",
        "forumAlias":"relationship",
        "nsfw":false,
        "gender":"F",
        "replyTitle":"*",
        "reacted":null,
        "liked":false,
        "subscribed":false,
        "collected":false,
        "personaSubscribed":false,
        "mediaMeta":[],
        "read":false,
        "newComment":false,
        "currentMember":false,
        "reactions":[
            {"id":"286f599c-f86a-4932-82f0-f5a06f1eca03","count":7056},
            {"id":"e8e6bc5d-41b0-4129-b134-97507523d7ff","count":250},
            {"id":"011ead16-9b83-4729-9fde-c588920c6c2d","count":6},
            {"id":"4b018f48-e184-445f-adf1-fc8e04ba09b9","count":2},
            {"id":"514c2569-fd53-4d9d-a415-bf0f88e7329f","count":1}
        ],
        "hidden":false,
        "customStyle":null,
        "isSuspiciousAccount":false,
        "isModerator":false,
        "layout":"classic",
        "spoilerAlert":false,
        "totalCommentCount":227,
        "withImages":false,
        "withVideos":false,
        "media":[],
        "reportReasonText":"",
        "excerptComments":[],
        "postAvatar":"",
        "verifiedBadge":false,
        "memberType":""
    }
]
```
### NEWS API


### PyPtt

### Data Process Pseudo Code
```python
def get_data(data_from, forum)
  data = request from API
  data = data.convert_json
  
  words is list
  for item in data:
    words append jieba.process(item)
    
  return words
```

## Result
![image]()

## Reference
1. [Dcard API](https://blog.jiatool.com/posts/dcard_api_v2/)
2. [PyPtt](https://github.com/PttCodingMan/PyPtt)
3. [NEWS API](https://newsapi.org/)
4. [jieba](https://github.com/fxsjy/jieba)
5. [WordCloud](https://amueller.github.io/word_cloud)
6. [tkinter document](https://tkdocs.com/)
