import getdata
import serial
from time import sleep

def scrollresult(result):
    COM_PORT = 'COM3'  # 請自行修改序列埠名稱
    BAUD_RATES = 9600
    ser = serial.Serial(COM_PORT, BAUD_RATES)
    try:
        if result == 'a':
            print('Glass')
            ser.write(b'Glass\n')  # 訊息必須是位元組類型
            sleep(0.5)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
            ser.close()
        elif result == 'b':
            print('Plastic')
            ser.write(b'Plastic\n')
            sleep(0.5)
            ser.close()
        elif result == 'c':
            print('PC')
            ser.write(b'PC\n')
            sleep(0.5)
            ser.close()
        elif result == 'd':
            print('IA')
            ser.write(b'IA\n')
            sleep(0.5)
            ser.close()
        elif result == 'e':
            print('GG')
            ser.write(b'GG\n')
            sleep(0.5)
            ser.close()
        elif result == 'f':
            print('Battery')
            ser.write(b'Battery\n')
            sleep(0.5) 
            ser.close()           
        else:
            print('指令錯誤…')
            
    except KeyboardInterrupt:
        ser.close()
        print('再見！')