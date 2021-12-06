from utility.record.txt import *

# //判斷txt是什麼紀錄
def record_txt(txt, line_id):
    txts = Txt(line_id)

    if txt == '本日紀錄':
        return txts.today()
    elif txt == '本周紀錄':
        return txts.week()
    elif txt == '本月紀錄':
        return txts.month()
    elif txt == '累積紀錄':
        return txts.acc()
