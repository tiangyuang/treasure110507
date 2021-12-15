from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

# ----------------------------------------------------
from utility.location import *
from utility.add_friend import *
from utility.location import *
from utility.problem import *
from utility.qr_verify import *
from utility.point import *
# record
from utility.record.record import *
# ----------------------------------------------------
from datetime import datetime
# CV
from utility.custom_vision.getdata import getData

# access token & channel secret
# line_bot_api物件:「操作」訊息，回應、發送、取得用戶資料
# handler物件:「處理」訊息，解讀或包裝訊息內容
line_bot_api = LineBotApi(
    '7DYharYqY7fWsn99AGi6mXtYl92Mya5iRvJTTwxyqZTZxIGARoGBGBJSgNPvA0I9uqM93g5MtlhqRhvcLRZ+2iwT8HDVoyr1BgaFobqCyKh/Y0wcC+v4dzyiSEzplTG/h1+Lrv93z+ECOWhnbkWMmgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9027ee6b55dbfa011d129a0e232c7fe8')

app = Flask(__name__)

# bot處理瀏覽首頁的請求


@app.route("/")
def index():
    photo = request.args.get('photo')
    getData(photo)

    return photo


# 接收post方法請求
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']  # 取HTTP標頭的密鑰欄位
    body = request.get_data(as_text=True)  # 取HTTP body並轉成文字格式

    try:
        handler.handle(body, signature)  # 結合body&金鑰驗證來源
    except InvalidSignatureError:  # 若驗證來源失敗，傳回400中斷連接
        abort(400)

    return 'OK'

# 接收任意類型LINE訊息的裝飾函式，程式沒意料到的


@handler.default()
def default(event):  # 接收「訊息事件」的參數 = 被包裝成MessageEvent的webhook事件物件(JSON)
    print('捕捉到事件：', event)

# //-----------------------------
# //Start------------------------
# //-----------------------------


# //處理加入好友事件[回傳加入好友json]
@handler.add(FollowEvent)
def handle_follow(event):
    print('加入好友follow：', event)
    line_bot_api.reply_message(
        event.reply_token, FlexSendMessage('confirm_add', confirm_add()))
# (處理訊息事件, 訊息類型=文字)
# def 函式名稱(event=JSON資料=Webhook事件物件)


#!接受QRCODE照片-----------
@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    message_content = line_bot_api.get_message_content(event.message.id)

    # //解析QRCODE照片
    line_id, mcode = decodeQR(event.source.user_id, message_content)

    recycling_time = datetime.fromtimestamp(int(str(event.timestamp)[:-3]))

    # //新增回收紀錄至DB

    line_bot_api.reply_message(
        event.reply_token, add_record(line_id, mcode, recycling_time))
#!-------------------------

# //處理各種文字


@handler.add(MessageEvent)
def handle_message(event):
    txt = event.message.text
    line_id = event.source.user_id

    # //打開相機-----------------
    if txt == 'qrcode':
        line_bot_api.reply_message(event.reply_token, open_camera())

    # //紀錄-----------------
    elif '紀錄' in txt:
        print('紀錄查詢:', event)
        line_bot_api.reply_message(event.reply_token, record_txt(txt, line_id))

    # //點數-----------------
    if txt == '點數兌換':
        print('點數:', event)

        line_bot_api.reply_message(event.reply_token, FlexSendMessage('friend', point_json(line_id)))

    # //通報-----------------
    if ('通報' in txt or txt[0] == "!"):
        problem_time = datetime.fromtimestamp(int(str(event.timestamp)[:-3]))
        print(problem_time)
        line_bot_api.reply_message(
            event.reply_token, problem_txt(txt, line_id, problem_time))

    # //加入好友[填寫基本資料json]
    line_bot_api.reply_message(event.reply_token, friend(txt, line_id))

    # //-------------------------


@handler.add(PostbackEvent)
def handle_Postback(event):
    line_bot_api.reply_message(event.reply_token, friend(
        '確認生日', 0, str(event.postback.params)[10:20]))


# //接收user地點 return附近垃圾桶[3]
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    lat = str(event.message.latitude)  # user緯度
    lng = str(event.message.longitude)  # user經度

    line_bot_api.reply_message(
        event.reply_token, FlexSendMessage('3location', location(lat, lng)))

# //-------------------------


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
