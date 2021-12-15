# python
import os.path
import time
import json
# line
from linebot.models import *
# utility
from utility import DB
from utility.record.txts.public.sum_point import sum_point
# pie
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# font
from matplotlib.font_manager import FontProperties

#// 製作圓餅圖
class Pie:
    def __init__(self, txt, line_id):
        self.txt = txt
        self.line_id = line_id

    def pie_quantity(self):
        if self.txt == '本月紀錄':
            quantity = DB.run(('SELECT c.Type_Number,ifnull(ct,0) FROM treasure_type as c left join(SELECT Sub_Type_number,count(Sub_Type_number) as ct FROM treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number where a.Record_LINEid="%s" and month(a.Record_Recycling_time)=month(now()) group by Sub_Type_number) as e on c.Type_Number = e.Sub_Type_number' % (self.line_id)), '1')
        else:
            quantity = DB.run(('SELECT c.Type_Number,ifnull(ct,0) FROM treasure_type as c left join(SELECT Sub_Type_number,count(Sub_Type_number) as ct FROM treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number where a.Record_LINEid="%s" group by Sub_Type_number) as e on c.Type_Number = e.Sub_Type_number' % (self.line_id)), '1')
        return quantity

    # //畫圓餅圖
    def draw_pie(self):
        quantity = self.pie_quantity()

        # 取得現在時間
        localtime = time.localtime()
        ptime = time.strftime("%Y%m%d_%H%M%S", localtime)

        # 指定使用字型和大小
        myFont = FontProperties(
            fname='C:/Users/Dolly/AppData/Roaming/Python/Python38/site-packages/matplotlib/mpl-data/fonts/ttf/TaipeiSansTCBeta-Regular.ttf', size=14)

        # 設定圓餅圖大小
        fig = plt.figure(figsize=(5, 5))
        # 將資料庫資料分割
        df = pd.DataFrame(quantity, columns=['type', 'qty'])
        print(df)
        # 將數量為0轉成nan
        df = df.replace(0, np.nan)
        print(df)
        # 將nan 丟掉
        df = df.dropna()

        # 設定顏色
        color = []

        for index, row in df.iterrows():
            if row["type"] == 'a':
                color.append('#EDBBBC')
            elif row["type"] == 'b':
                color.append('#F8BA91')
            elif row["type"] == 'c':
                color.append('#FDDB7E')
            elif row["type"] == 'd':
                color.append('#B3D89B')
            elif row["type"] == 'e':
                color.append('#A8C3D9')
            else:
                color.append('#CBA9D9')

        # 設定圓餅圖屬性
        a, category_text, percent_text = plt.pie(
            df['qty'],                      # 數值
            colors=color,                   # 指定圓餅圖的顏色
            autopct="%0.0f%%",              # 四捨五入至小數點後面位數
            pctdistance=0.65,               # 數值與圓餅圖的圓心距離
            radius=1.5,                     # 圓餅圖的半徑，預設是1
            shadow=False)                   # 是否使用陰影

        # 把每個分類設成中文字型
        for t in category_text:
            t.set_fontproperties(myFont)
            t.set_size(20)

        # 把每個數值設成中文字型
        for t in percent_text:
            t.set_fontproperties(myFont)
            t.set_size(16)

        # 畫出圓餅圖
        plt.savefig(os.path.join('static\pie', self.line_id+ptime+".jpg"))

        ngrok = 'https://e750-2001-b400-e3d2-1822-356d-72c3-448f-7764.ngrok.io/'

        pie_path = f'{ngrok}static/pie/{self.line_id}{ptime}.jpg'
        print('=================================0000000000000000000============')
        print(pie_path)

        return pie_path


    def pie_json(self,pie_path):
        
        # month_record = (('a', '玻璃', 14), ('b', '塑膠', 31), ('c', '紙容器', 4), ('d', '鐵鋁', 23), ('e', '一般垃圾', 9), ('f', '電池', 24))
        # line_id = 'U0131826f2d23e1f17a3689d8574fd2cb'

        div = []

        month_record = self.pie_quantity()

        # month_record = DB.run(("select d.Type_Number,d.Type_Name ,count(d.Type_Name) from treasure.treasure_recycling_record as a join treasure.treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure.treasure_erection_location as c on a.Record_Location_number=c.Location_Number join treasure.treasure_type as d on b.Sub_Type_number = d.Type_Number where a.Record_LINEid='%s' and month(a.Record_Recycling_time)=month(now()) group by d.Type_Name order by d.Type_Number " % (self.line_id)), '1')

        div.append({"type": "box",
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
                        "text": f'玻璃 {month_record[0][1]}',
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
                        "text": f'塑膠 {month_record[1][1]}',
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
                        "text": f'紙容器 {month_record[2][1]}',
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
                        "text": f'鐵鋁 {month_record[3][1]}',
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
                        "text": f'一般 {month_record[4][1]}',
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
                        "text": f'電池 {month_record[5][1]}',
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
                # print(div)

        

                # print(data['body']['contents'][1])

        if self.txt == '本月紀錄':
            with open('json/record_month.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                data['header']['contents'][0]['contents'][2]['text']= sum_point(self.line_id)   #點數
                data['body']['contents'][0]['url'] = pie_path    #圖片url
                print('0000000000000000000000000000000000000')
                print(pie_path)
                data['body']['contents'][1]= div[0] #數量
                
            with open('json/record_month.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file)

            pie_record = json.load(open('json/record_month.json', 'r', encoding='utf-8'))
        
        else:
            with open('json/record_acc.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                data['header']['contents'][0]['contents'][2]['text']= sum_point(self.line_id)    #點數
                data['body']['contents'][0]['url'] = pie_path    #圖片url
                
                data['body']['contents'][1]= div[0] #數量
                
            with open('json/record_acc.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file)


            pie_record = json.load(open('json/record_acc.json', 'r', encoding='utf-8'))

        return(pie_record)

