from utility.record.txts.today import *
from utility.record.txts.week import *
from utility.record.txts.month import *
from utility.record.txts.acc import *

# // Class Txt 以line_id製作紀錄查詢的json

class Txt:
    def __init__(self, line_id):
        self.line_id = line_id

    def today(self):
        return today(self.line_id)

    def week(self):
        return week(self.line_id)

    def month(self):
        return month(self.line_id)

    def acc(self):
        return acc(self.line_id)
