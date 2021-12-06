
import DB
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime as dt
from datetime import timedelta as delta
import json
import os.path
# import字型管理套件

from matplotlib.font_manager import FontProperties


def type_qty(month_record):
    for i in range(len(month_record)):
        month_record[i][0]

line_id = 'U0131826f2d23e1f17a3689d8574fd2cb'

div = []
month_record = DB.run(("select d.Type_Name ,count(d.Type_Name) from treasure.treasure_recycling_record as a join treasure.treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure.treasure_erection_location as c on a.Record_Location_number=c.Location_Number join treasure.treasure_type as d on b.Sub_Type_number = d.Type_Number where a.Record_LINEid='%s' and month(a.Record_Recycling_time)=month(now()) group by d.Type_Name" % (line_id)), '1')
print(month_record)
for i in range(len(month_record)):
    div.append({
        "type": "image",
        "size": "full",
        "offsetEnd": "lg",
        "url": "https://064b-112-78-72-254.ngrok.io/static/pie/20211022_175951.jpg"
        },
        {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/LOF5157.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "玻璃 5",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/25MddyP.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "塑膠 12",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/KyGEQ40.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "紙容器 5",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/bTsktLu.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "鐵鋁 3",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/uqBNvcP.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "一般 0",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://imgur.com/9ZVr3MB.jpg",
                        "size": "xs",
                        "offsetTop": "7%"
                    },
                    {
                        "type": "text",
                        "text": "電池 2",
                        "wrap": True,
                        "size": "15px",
                        "color": "#000000"
                    }
                ],
                "spacing": "md",
                "margin": "md"
            }
        ],
        "width": "25%"
    })

with open('src/json/record_month.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    # data['contents'][0]['header']['contents'][0]['contents'][2]['text'] = record_sum_point(line_id)
    # data['contents'][0]['body']['contents'] = div
    data['header']['contents'][0]['contents'][2]['text'] = '1.15'
    # print(data['body']['contents'])
# with open('src/json/record_week.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file)
