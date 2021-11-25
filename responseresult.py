import getdata
import serial
from time import sleep

 
COM_PORT = 'COM10'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

# try:
    # while True:
        # 接收用戶的輸入值並轉成小寫
def responsersult(result):
    try:
        if result == 'a':
            print('Glass')
            ser.write(b'Glass\n')  # 訊息必須是位元組類型
            sleep(0.5)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif result == 'b':
            print('Plastic')
            ser.write(b'Plastic\n')
            sleep(0.5)
        elif result == 'c':
            print('PC')
            ser.write(b'PC\n')
            sleep(0.5)
        elif result == 'd':
            print('IA')
            ser.write(b'IA\n')
            sleep(0.5)
        elif result == 'e':
            print('GG')
            ser.write(b'GG\n')
            sleep(0.5)
        elif result == 'f':
            print('Battery')
            ser.write(b'Battery\n')
            sleep(0.5)            
        else:
            print('指令錯誤…')

        # while ser.in_waiting:
        #     mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        #     print('控制板回應：', mcu_feedback)
            
    except KeyboardInterrupt:
        ser.close()
        print('再見！')