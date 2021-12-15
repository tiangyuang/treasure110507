import pymysql
import time
import os
import shutil
from utility import DB


def datastore(result, imgFile, url):
    # 計時開始
    start = time.time()

    # //流水號
    sn = DB.run('SELECT max(Sub_Serial_number) FROM treasure.treasure_sub_record','2')[0]+1

    # //得到點數
    gt = DB.run(('SELECT Type_Points FROM treasure_type where Type_Number="%s"' % (result)),'2')[0]
    
    # //目前使用者
    SSn = DB.run('SELECT max(Record_Recycling_number) FROM treasure.treasure_recycling_record','2')[0]

    #// 新增資料
    DB.run('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points , Sub_Picture) '
               'VALUES (%d,"%s","%s",%.2f,"%s")' %(sn, SSn, result, gt, url))


    today = time.strftime('%Y%m%d_%H_%M_%S')
    shutil.copy(imgFile, "utility/custom_vision/pic/result/"+str(today)+"_"+result+".jpg")
    os.remove(imgFile)
    # 計時結束
    end = time.time()
    total = end-start
    print(total)
