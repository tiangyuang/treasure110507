# python
from datetime import datetime as dt
import json

from linebot.models import *
import qrcode
import random
import zxing
import time

# utility
from utility import DB
from utility.record.record import record_txt
from utility.record.txts.public.icon import icon
from utility.record.txts.public.sum_point import sum_point
from utility.door import door


# //資料庫取得mcode 製作QRcode
def mcodeQR():
    mcode = DB.run(
        'SELECT Location_Machinecode FROM treasure_erection_location', '1')
    for i in range(len(mcode)):
        randomQR = random.randint(1, 5)
        randomborder = random.randint(4, 11)
        if randomQR == 1:
            qr = qrcode.QRCode(
                version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=randomborder)
        elif randomQR == 2:
            qr = qrcode.QRCode(
                version=3, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=randomborder)
        elif randomQR == 3:
            qr = qrcode.QRCode(
                version=3, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=randomborder)
        else:
            qr = qrcode.QRCode(
                version=3, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=randomborder)

        qr.add_data(mcode[i][0])
        qr.make(fit=True)
        img = qr.make_image()
        img.save(f'src/static/qr_img/QR{i+1}.jpg')

    return 0

# //開啟相機


def open_camera():
    emoji = [
        {
            "index": 0,
            "productId": "5ac21e6c040ab15980c9b444",
            "emojiId": "082"
        },
        {
            "index": 8,
            "productId": "5ac22e85040ab15980c9b44f",
            "emojiId": "045"
        },
        {
            "index": 18,
            "productId": "5ac2264e040ab15980c9b44b",
            "emojiId": "222"
        },
        {
            "index": 35,
            "productId": "5ac2280f031a6752fb806d65",
            "emojiId": "001"
        },
        {
            "index": 36,
            "productId": "5ac22775040ab15980c9b44c",
            "emojiId": "244"
        }

    ]
    camera = TextSendMessage(
        text='$點擊開啟相機\n$拍攝QRcode\n$等待閘門打開\n就可以開始回收啦~$$',
        emojis=emoji,
        quick_reply=QuickReply
        (
            items=[
                QuickReplyButton(
                    action=CameraAction(
                        label="開啟相機",
                        text="text"
                    )
                )
            ]
        )
    )

    return camera


# //解讀 userQR
def decodeQR(line_id, message_content):
    with open('static/qr_img/1.jpg', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    reader = zxing.BarCodeReader()
    barcode = reader.decode('static/qr_img/1.jpg')

    return line_id, barcode.parsed


# //透過Line_id檢查是否有此user 確認DB有沒有此會員
def check_user_db(line_id):
    check = DB.run(
        "SELECT Member_LINEid FROM treasure.treasure_member where Member_LINEid = '%s'" % (line_id), '2')
    if len(check) == 1:
        return True


# //新增回收紀錄至DB
def add_record(line_id, mcode, recycling_time):
    # //有此user的話，add總紀錄
    if check_user_db(line_id):
        recycling_number = DB.run(
            "SELECT max(Record_Recycling_number)+1 FROM treasure.treasure_recycling_record", '2')[0]
        location_number = DB.run(
            ("SELECT Location_Number  FROM treasure.treasure_erection_location where Location_Machinecode ='%s'") % (mcode), '1')[0][0]

        DB.run('INSERT INTO treasure_recycling_record (Record_Recycling_number , Record_LINEid , Record_Location_number , Record_Recycling_time)' 'VALUES (%d,"%s",%d,"%s")' % (
            recycling_number, line_id, location_number, recycling_time))
        # 開門
        door()

    else:
        return 'hhhhhhh'

        #!開門
        #! return TextSendMsg() 告訴user可以回收，讓他選擇回收完畢or取消回收


# //查詢現在回收紀錄
def now_record(line_id):
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

# //製作現在紀錄json
def __json(line_id):
    recycle_number = DB.run(("SELECT Record_Recycling_number FROM treasure.treasure_recycling_record where Record_LINEid = '%s' order by Record_Recycling_number desc" %(line_id)),'2')[0]
    record_now = DB.run(("select d.Type_Name,b.Sub_Get_points,a.Record_Recycling_time,c.Location_Name,b.Sub_Picture from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number join treasure_type as d on b.Sub_Type_number = d.Type_Number join treasure_erection_location as c on a.Record_Location_number=c.Location_Number where a.Record_LINEid= '%s' and Sub_Recycling_number = '%s'" % (line_id,recycle_number)), '1')
    
    div = []
    for i in range(len(record_now)):
        record_date = record_now[i][2]
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
                                        "url": icon(record_now[i][0])
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
                                                "text": record_now[i][0],
                                                "weight": "bold",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": f'+{record_now[i][1]}',
                                                "align": "end",
                                                "offsetEnd": "21px",
                                                "color": "#16BB54"
                                            }
                                        ],
                                        "justifyContent": "space-around"
                                    },
                                    {
                                        "type": "text",
                                        "text": f'{date} , {record_now[i][3][3:]} , {time}',
                                        "size": "15px"
                                    }
                                ],
                                "flex": 3
                            }
                        ]
                    },
                    {
                        "type": "image",
                        "url": record_now[i][4],
                        "size": "xl",
                        "margin": "sm"
                    }
                ],
                "paddingTop": "1%",
                "spacing": "sm"
            }
        }
        )

    print(div)
    with open('json/record_now.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['contents'] = div

    with open('json/record_now.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    search_record = json.load(
        open('json/record_now.json', 'r', encoding='utf-8'))

    return search_record
