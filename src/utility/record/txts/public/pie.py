# python
import os.path
import time
# line
from linebot.models import *
# utility
from utility import DB
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
        pie_quantity = self.pie_quantity()

        if self.txt == '本月紀錄':
            quantity = pie_quantity
        else:
            quantity = pie_quantity

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
        plt.savefig(os.path.join('src\static\pie', self.line_id+ptime+".jpg"))
