# python
import json
# line
from linebot.models import *
# utility
from utility.record.txts.public.pie import Pie


# //顯示累積按鈕與累積紀錄
def acc(line_id):
    # 畫圓餅圖
    pie = Pie('累積紀錄',line_id)
    pie_math=pie.draw_pie()

    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/g0WeLP1.png',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=110, width=1040),
        actions=[
            MessageImagemapAction(
                text='本日紀錄',
                area=ImagemapArea(
                    x=4, y=8, width=175, height=92
                )
            ),
            MessageImagemapAction(
                text='本周紀錄',
                area=ImagemapArea(
                    x=205, y=8, width=154, height=92
                )
            ),
            MessageImagemapAction(
                text='本月紀錄',
                area=ImagemapArea(
                    x=402, y=8, width=160, height=96
                )
            ),
            MessageImagemapAction(
                text='累積紀錄',
                area=ImagemapArea(
                    x=598, y=8, width=147, height=96
                )
            )
        ]
    )
    return[FlexSendMessage('record_today', pie.pie_json(pie_math)), imagemap_today]
