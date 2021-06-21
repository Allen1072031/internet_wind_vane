from PyPtt import PTT
import jieba.analyse
from api import variable


def get_data(ptt_id: str, password: str, board_list=None):
    if board_list is None:
        board_list = ["Gossiping"]
    ptt_bot = PTT.API()

    try:
        ptt_bot.login(ptt_id, password)
    except PTT.exceptions.LoginError:
        ptt_bot.log('登入失敗')
    except PTT.exceptions.WrongIDorPassword:
        ptt_bot.log('帳號密碼錯誤')
    except PTT.exceptions.LoginTooOften:
        ptt_bot.log('請稍等一下再登入')
    ptt_bot.log('登入成功')
    if ptt_bot.unregistered_user:
        print('未註冊使用者')
        if ptt_bot.process_picks != 0:
            print(f'註冊單處理順位 {ptt_bot.process_picks}')
    if ptt_bot.registered_user:
        print('已註冊使用者')

    # crawler
    data = []

    def crawl_handler(post_info):
        data.append(post_info.title)
        data.append(post_info.content)
        for push_info in post_info.push_list:
            data.append(push_info.content)
        variable.crawl_processing += 1

    for board in board_list:
        newest_index = ptt_bot.get_newest_index(
            PTT.data_type.index_type.BBS,
            board=board,
            search_type=PTT.data_type.post_search_type.PUSH,
            search_condition="75",
        )
        crawl_range = 20
        start_index = newest_index - crawl_range + 1
        variable.crawl_end = crawl_range

        ptt_bot.crawl_board(
            PTT.data_type.crawl_type.BBS,
            crawl_handler,
            board=board,
            start_index=start_index,
            end_index=newest_index,
            search_type=PTT.data_type.post_search_type.PUSH,
            search_condition="75"
        )

    ptt_bot.logout()

    words = []
    for item in data:
        if item:
            word_list = jieba.analyse.extract_tags(item)
            words += word_list

    return words
