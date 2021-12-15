import json
from utility.record.txts.public.sum_point import sum_point

def point_json(line_id):
    with open('json/point.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['contents'][0]['header']['contents'][0]['contents'][2]['text'] = sum_point(line_id)

    with open('json/point.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    search_record = json.load(open('json/point.json', 'r', encoding='utf-8'))

    return search_record