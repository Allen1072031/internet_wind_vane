from PyPtt import PTT
import sys


if __name__ == '__main__':
    ptt_id = "*"
    password = "*"

    ptt_bot = PTT.API()
    try:
        ptt_bot.login(ptt_id, password)
    except PTT.exceptions.LoginError:
        ptt_bot.log('登入失敗')
        sys.exit()
    except PTT.exceptions.WrongIDorPassword:
        ptt_bot.log('帳號密碼錯誤')
        sys.exit()
    except PTT.exceptions.LoginTooOften:
        ptt_bot.log('請稍等一下再登入')
        sys.exit()
    ptt_bot.log('登入成功')

    if ptt_bot.unregistered_user:
        print('未註冊使用者')
        if ptt_bot.process_picks != 0:
            print(f'註冊單處理順位 {ptt_bot.process_picks}')

    if ptt_bot.registered_user:
        print('已註冊使用者')

    # call ptt_bot other api
    post_info = ptt_bot.get_post(
        'Python',
        post_index=7486)
    print(post_info.content)

    test_board_list = [
        'Wanted',
        'Gossiping',
        'Test',
        'Stock',
        'movie',
    ]

    for test_board in test_board_list:
        index = ptt_bot.get_newest_index(
            PTT.data_type.index_type.BBS,
            board=test_board
        )
        print(f'{test_board} 最新文章編號 {index}')

    ptt_bot.logout()
