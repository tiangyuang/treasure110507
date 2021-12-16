from linebot.models import *
from utility import DB


def problem_txt(txt, line_id, problem_time):
    global problem_location
    # //詢問哪裡出問題
    if txt == '問題通報':
        return problem()

    # //處理通報的文字描述
    elif '通報地點' in txt:
        problem_location = txt[5:]
        problem_buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgur.com/xGcNmFo.png',
                title='描述問題',
                text='也可以先打!再輸入文字\n例如:!無法登入',
                actions=[
                    MessageAction(
                        label='辨識錯誤',
                        text='!辨識錯誤'
                    ),
                    MessageAction(
                        label='閘門打不開',
                        text='!閘門打不開'
                    ),
                    MessageAction(
                        label='無法開啟相機',
                        text='!無法開啟相機'
                    )
                ]
            )
        )

        return problem_buttons_template_message

    elif txt[0] == "!":
        Service_Problem = txt[1:]
        problem_to_db(line_id, problem_location, Service_Problem, problem_time)
        # problem_to_db(line_id,problem_time,problem_location,Service_Problem)
        emoji = [
        {
            "index": 0,
            "productId": "5ac21a18040ab15980c9b43e",
            "emojiId": "025"
        },
        {
            "index": 7,
            "productId": "5ac2280f031a6752fb806d65",
            "emojiId": "101"
        }
        ]
        return TextSendMessage(text='收到通報了，我們會盡快處理的')

        # pp = TextSendMessage(text='$我們收到通報了，我們會盡快處理的$',emojis=emoji)

        # return pp
        


# // 將問題新增至DB
def problem_to_db(line_id, problem_location, Service_Problem, problem_time):
    DB.run('INSERT INTO treasure.treasure_service (Service_LINEid, Service_Location, Service_Problem,Service_time) VALUES ("%s","%s","%s","%s")' % (
        line_id, problem_location, Service_Problem, problem_time))


# //詢問哪裡出問題
def problem():
    emoji = [
        {
            "index": 0,
            "productId": "5ac21a18040ab15980c9b43e",
            "emojiId": "025"
        },
        {
            "index": 7,
            "productId": "5ac2280f031a6752fb806d65",
            "emojiId": "101"
        }
    ]
    where = TextSendMessage(
        text='$哪裡出問題了$',
        emojis=emoji
    )

    imagemap_where = ImagemapSendMessage(
        base_url='https://i.imgur.com/bziXxW8.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1000, width=1040),
        actions=[
            MessageImagemapAction(
                text='通報地點:台北市中正區',
                area=ImagemapArea(
                    x=135, y=97, width=171, height=101
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市中山區',
                area=ImagemapArea(
                    x=324, y=91, width=158, height=105
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市大安區',
                area=ImagemapArea(
                    x=504, y=97, width=161, height=101
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市士林區',
                area=ImagemapArea(
                    x=141, y=276, width=163, height=101
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市萬華區',
                area=ImagemapArea(
                    x=335, y=270, width=143, height=109
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市大同區',
                area=ImagemapArea(
                    x=516, y=272, width=137, height=105
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市信義區',
                area=ImagemapArea(
                    x=145, y=457, width=155, height=101
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市松山區',
                area=ImagemapArea(
                    x=329, y=456, width=153, height=98
                )
            ), MessageImagemapAction(
                text='通報地點:台北市內湖區',
                area=ImagemapArea(
                    x=508, y=451, width=149, height=109
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市北投區',
                area=ImagemapArea(
                    x=143, y=633, width=161, height=107
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市南港區',
                area=ImagemapArea(
                    x=327, y=627, width=157, height=111
                )
            ),
            MessageImagemapAction(
                text='通報地點:台北市文山區',
                area=ImagemapArea(
                    x=502, y=629, width=161, height=109
                )
            )
        ]
    )
    return [where, imagemap_where]
