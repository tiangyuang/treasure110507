
import DB
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime as dt
from datetime import timedelta as delta

import os.path
# import字型管理套件

from matplotlib.font_manager import FontProperties

line_id = 'U0131826f2d23e1f17a3689d8574fd2cb'


# 指定使用字型和大小

myFont = FontProperties(fname='C:/Users/Dolly/AppData/Roaming/Python/Python38/site-packages/matplotlib/mpl-data/fonts/ttf/TaipeiSansTCBeta-Regular.ttf', size=14)


# 設定顏色

color = ['#EDBBBC', '#F8BA91', '#FDDB7E', '#B3D89B', '#A8C3D9', '#808ef9']


quantity = DB.run(('select d.Type_Name ,count(d.Type_Name) from treasure.treasure_recycling_record as a join treasure.treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure.treasure_erection_location as c on a.Record_Location_number=c.Location_Number join treasure.treasure_type as d on b.Sub_Type_number = d.Type_Number where a.Record_LINEid="%s" and month(a.Record_Recycling_time)=month(now()) group by d.Type_Name' % (line_id)), '1')

localtime = time.localtime()
ptime = time.strftime("%Y%m%d_%H%M%S", localtime)

# 設定圓餅圖大小
fig = plt.figure(figsize=(5, 5))

df = pd.DataFrame(quantity,columns=['country', 'type'])

# 設定圓餅圖屬性
a, category_text, percent_text = plt.pie(
    df['type'],
    # labels=df['country'],                       # 數值
    colors=color,                   # 指定圓餅圖的顏色
    autopct="%0.0f%%",              # 四捨五入至小數點後面位數
    pctdistance=0.65,               # 數值與圓餅圖的圓心距離
    radius=1.5,                     # 圓餅圖的半徑，預設是1
    shadow=False)                     # 是否使用陰影

# 把每個分類設成中文字型

for t in category_text:
    t.set_fontproperties(myFont)
    t.set_size(20)

# 把每個數值設成中文字型

for t in percent_text:
    t.set_fontproperties(myFont)
    t.set_size(16)


# 畫出圓餅圖
plt.savefig(os.path.join('treasure110507\static\pie', line_id+ptime+".jpg"))



# fileTest = ("treasure110507/static/pie/p1.jpg")
# time.sleep(5)
# os.remove(fileTest)