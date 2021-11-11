import pymysql
import getdata
import time
import os,shutil

def datastore(result, imgFile, url):

    #計時開始
    start=time.time()
    #資料庫連線
    db=pymysql.connect(host="treasuredb.mysql.database.azure.com",user="ntubimdtreasure@treasuredb",passwd="Treasure110507",db="treasure",port=3306,charset='utf8')
    cursor=db.cursor()

    #流水號
    serial=('SELECT max(Sub_Serial_number) FROM treasure.treasure_sub_record')
    cursor.execute(serial)
    sn=cursor.fetchall()[0][0]+1

    #得到點數
    getpoint=('SELECT Type_Points FROM treasure_type where Type_Number="%s"' % result)
    cursor.execute(getpoint)
    gt=cursor.fetchall()[0][0]


    #新增資料
    sqlcode=('INSERT INTO treasure_sub_record (Sub_Serial_number , Sub_Recycling_number , Sub_Type_number , Sub_Get_points , Sub_Picture) ' 
    'VALUES (%d,"%s","%s",%.2f,"%s")')    

    #資料內容
    data=(sn,5,result,gt,url)
    cursor.execute(sqlcode % data)

    print(data)

    #----------------------------------------------------------
    db.commit()

    db.close()

    today=time.strftime('%Y%m%d_%H_%M_%S')
    shutil.copy(imgFile,"C:/Users/vince/OneDrive/桌面/Treasure110507/picture-testing/"+str(today)+"_"+result+".jpg")
    shutil.move("C:/Users/vince/OneDrive/桌面/Treasure110507/picture-testing/"+str(today)+"_"+result+".jpg","C:/Users/vince/OneDrive/桌面/Treasure110507/picture-result")
    os.remove(imgFile)
    #計時結束
    end=time.time()
    total=end-start
    print(total)
