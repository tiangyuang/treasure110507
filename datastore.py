import pymysql
import getdata
import time
import os
import shutil


def datastore(result, imgFile, url):

    # 計時開始
    start = time.time()
    # 資料庫連線
    db = pymysql.connect(host="treasuredb2.mysql.database.azure.com", user="joe21255797",
                        passwd="Treasure110507", database="treasure", port=3306, ssl={'ca': 'DigiCertGlobalRootCA.crt.pem'})
    cursor = db.cursor()

    # 流水號
    serial = ('SELECT max(Sub_Serial_number) FROM treasure.treasure_sub_record')
    cursor.execute(serial)
    sn = cursor.fetchall()[0][0]+1

    # 得到點數
    getpoint = (
        'SELECT Type_Points FROM treasure_type where Type_Number="%s"' % result)
    cursor.execute(getpoint)
    gt = cursor.fetchall()[0][0]

    # 新增資料
    sqlcode = ('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points , Sub_Picture) '
               'VALUES (%d,"%s","%s",%.2f,"%s")')

    #目前使用者
    SSnsql=("SELECT max(Record_Recycling_number) FROM treasure.treasure_recycling_record")
    cursor.execute(SSnsql)
    SSn = cursor.fetchall()[0][0]
    
    # 資料內容
    data = (sn, SSn, result, gt, url)
    cursor.execute(sqlcode % data)

    print(data)

    # ----------------------------------------------------------
    db.commit()

    db.close()

    today = time.strftime('%Y%m%d_%H_%M_%S')
    shutil.copy(imgFile, "./pic/testing/"+str(today)+"_"+result+".jpg")
    shutil.move("./pic/testing/"+str(today)+"_"+result+".jpg", "./pic/result")
    os.remove(imgFile)
    # 計時結束
    end = time.time()
    total = end-start
    print(total)
