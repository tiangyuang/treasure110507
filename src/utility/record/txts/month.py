# python
import json
# line
from linebot.models import *
# utility
from utility.record.txts.public.pie import Pie

# //顯示本月按鈕與本月紀錄
def month(line_id):
    # 畫圓餅圖
    pie = Pie('本月紀錄',line_id)
    pie.draw_pie()

    record_today = json.load(
        open('src/json/record_month.json', 'r', encoding='utf-8'))

    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/jHrl9VA.png',
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
    return[FlexSendMessage('record_today', record_today), imagemap_today]
