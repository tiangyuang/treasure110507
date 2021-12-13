# python
from datetime import datetime as dt
import json
# line
from linebot.models import *
# utility
from utility import DB
from utility.record.txts.public.icon import icon
from utility.record.txts.public.sum_point import sum_point


# //顯示本日按鈕與本日紀錄
def today(line_id):
    imagemap_today = ImagemapSendMessage(
        base_url='https://i.imgur.com/Z96l63C.png',
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
    return[FlexSendMessage('record_today', __json(line_id)), imagemap_today]

# //製作當日紀錄json
def __json(line_id):
    today_record = DB.run(("select d.Type_Name,b.Sub_Get_points,a.Record_Recycling_time,c.Location_Name,b.Sub_Picture from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure_type as d on b.Sub_Type_number = d.Type_Number join treasure_erection_location as c on a.Record_Location_number=c.Location_Number where a.Record_LINEid='%s' and date(a.Record_Recycling_time) = curdate()" % (line_id)), '1')

    div = []

    for i in range(len(today_record)):
        record_date = today_record[i][2]
        date = dt.strftime(record_date, '%Y/%m/%d')
        time = dt.strftime(record_date, '%H:%M')

        div.append({
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "text",
                                "text": "本日紀錄",
                                "weight": "bold",
                                "color": "#16BB54",
                                "size": "md"
                            },
                            {
                                "type": "icon",
                                "url": "https://imgur.com/UcfCKxf.png",
                                "size": "20px",
                                "offsetTop": "20%",
                                "offsetEnd": "xs"
                            },
                            {
                                "type": "text",
                                "text": sum_point(line_id),
                                "flex": 0,
                                "color": "#16BB54",
                                "weight": "bold"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    }
                ],
                "paddingTop": "15px",
                "height": "60px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "icon",
                                        "size": "40px",
                                        "url": icon(today_record[i][0])
                                    }
                                ],
                                "justifyContent": "flex-start",
                                "flex": 1
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": today_record[i][0],
                                                "weight": "bold",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": f'+{today_record[i][1]}',
                                                "align": "end",
                                                "offsetEnd": "21px",
                                                "color": "#16BB54"
                                            }
                                        ],
                                        "justifyContent": "space-around"
                                    },
                                    {
                                        "type": "text",
                                        "text": f'{date} , {today_record[i][3][3:]} , {time}',
                                        "size": "15px"
                                    }
                                ],
                                "flex": 3
                            }
                        ]
                    },
                    {
                        "type": "image",
                        "url": today_record[i][4],
                        "size": "xl",
                        "margin": "sm"
                    }
                ],
                "paddingTop": "1%",
                "spacing": "sm"
            }
        }
        )

    with open('treasure110507/json/record_today.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['contents'] = div

    with open('treasure110507/json/record_today.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    search_record = json.load(
        open('treasure110507/json/record_today.json', 'r', encoding='utf-8'))

    return search_record
