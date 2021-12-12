import pymysql

# *連接 MySQL 資料庫
# *run sql指令
def run(sql,type=0):
    print("db\t %s" %(sql))
    db = pymysql.connect(host="treasuredb2.mysql.database.azure.com", user="joe21255797",passwd="Treasure110507", database="treasure", port=3306,ssl={"fake_flag_to_enable_tls":True})
    
    # db = pymysql.connect(host="127.0.0.1",user="root", passwd="NTUB10656051", db="treasure",port=3306,charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)

    # !查詢 [1]
    if(type=="1"):
        return cursor.fetchall()
    elif(type=="2"):
        return cursor.fetchone()

    db.commit()
    db.close()
    print('connect ok')



