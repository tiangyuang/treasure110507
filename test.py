
from utility import DB

gt = DB.run(('SELECT Type_Points FROM treasure_type where Type_Number="%s"' % ('a')),'2')
print(gt[0])