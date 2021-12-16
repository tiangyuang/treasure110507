from linebot.models import *
import json

from utility import DB

# //Line[加入好友]
def confirm_add():
    confirm_add = json.load(
        open('json/confirm_add.json', 'r', encoding='utf-8'))
    return confirm_add

# //填寫基本資料json介面
def friend(txt, line_id=0, time=0):
    global  birthday, phone, name, address
    if txt == '加入好友':
        date_picker = TemplateSendMessage(
            alt_text='輸入生日',
            template=ButtonsTemplate(
                title='請輸入生日',
                text='生日',
                actions=[
                    DatetimePickerAction(
                        label='設定',
                        data='birthday',
                        mode='date',
                        initial='1995-04-01',
                        min='1920-04-01',
                        max='2020-12-31'
                    )
                ]
            )
        )
        return date_picker

    elif txt == '確認生日':
        birthday = time
        confirm_birthday = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text=f'您的生日是{time}嗎?',
                actions=[
                    MessageAction(
                        label='是',
                        text='是'
                    ),
                    MessageAction(
                        label='否',
                        text='否'
                    )
                ]
            )
        )
        return confirm_birthday

    elif txt in '是否':
        return TextSendMessage(text='請輸入您的手機號碼與姓名，ex:0912345678許大人')

    elif txt[0] == '0' and txt[1] == '9':
        phone = txt[:10]
        name = txt[10:]

        return TextSendMessage(text='請輸入您的地址，ex:台北市中正區')

    elif txt[2] == '縣' or txt[2] == '市':
        address = txt
        print(line_id, birthday, phone, address, name)

        (d) = become_friend(line_id, birthday, phone, address, name)
        if (d):
            print("success")
        else:
            print("fail")

        return TextSendMessage(text='成功')



# //將好友資料寫入DB
def become_friend(line_id, birthday, phone, address, name):
    DB.run("insert into treasure_member (Member_LINEid,Member_Birthady,Member_Phone,Member_Address,Member_Name) values(\"%s\", \"%s\",\"%s\",\"%s\",\"%s\")" % (
        line_id, birthday, phone, address, name))
    return 0



