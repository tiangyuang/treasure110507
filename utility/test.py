
import json
# //查詢現在回收紀錄

from record.txts.public.sum_point import sum_point

line_id = 'U0131826f2d23e1f17a3689d8574fd2cb'

with open('json/point.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    # print(data['contents'][0]['header']['contents'][0]['contents'][2]['text'])
    data['contents'][0]['header']['contents'][0]['contents'][2]['text'] = sum_point(line_id)


with open('json/point.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)

search_record = json.load(
    open('json/point.json', 'r', encoding='utf-8'))






