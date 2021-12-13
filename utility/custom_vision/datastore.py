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
    # getpoint = (
    #     'SELECT Type_Points FROM treasure_type where Type_Number="%s"' % result)
    # cursor.execute(getpoint)
    gt = DB.run(('SELECT Type_Points FROM treasure_type where Type_Number="%s"' % (result)),'2')[0]
    
    # //目前使用者
    # SSnsql=("SELECT max(Record_Recycling_number) FROM treasure.treasure_recycling_record")
    # cursor.execute(SSnsql)
    # SSn = cursor.fetchall()[0][0]
    SSn = DB.run('SELECT max(Record_Recycling_number) FROM treasure.treasure_recycling_record','2')[0]

    # 新增資料
    # sqlcode1 = ('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points , Sub_Picture) '
    #            'VALUES (%d,"%s","%s",%.2f,"%s")')

    sqlcode = DB.run('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points , Sub_Picture) '
               'VALUES (%d,"%s","%s",%.2f,"%s")' %(sn, SSn, result, gt, url))

    
    
    # # 資料內容
    # data = (sn, SSn, result, gt, url)
    # cursor.execute(sqlcode % data)

    # print(data)

    # # ----------------------------------------------------------
    # db.commit()

    # db.close()

    # today = time.strftime('%Y%m%d_%H_%M_%S')
    # shutil.copy(imgFile, "./pic/testing/"+str(today)+"_"+result+".jpg")
    # shutil.move("./pic/testing/"+str(today)+"_"+result+".jpg", "./pic/result")
    # os.remove(imgFile)
    # 計時結束
    end = time.time()
    total = end-start
    print(total)
