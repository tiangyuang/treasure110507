
from utility import DB

a = DB.run("SELECT Member_LINEid FROM treasure.treasure_member where Member_LINEid = 'U0131826f2d23e1f17a3689d8574fd2cb'",'1')
print(a[0][0])