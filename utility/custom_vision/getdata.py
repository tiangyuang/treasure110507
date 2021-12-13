from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time
import urllib.request

from utility.custom_vision.datastore import *
# from utility.custom_vision.datastore import datastore
# from utility.custom_vision.responseresult import responsersult 
# from utility.custom_vision.scrollresult import scrollresult
   
def getData(photo):
    print('=================================')     
    # print(dtest())
    start=time.time()

    # 傳入prediction-key及endpoint
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": 'ae5d89cda9ab489487077626758c7c4b'})
    predictor = CustomVisionPredictionClient(endpoint='https://treasureprediction.cognitiveservices.azure.com/', credentials=credentials)

    # 設定project.id, publish_iteration_name, 圖片位置及名稱
    PROJECT_ID = '01b046a9-37fd-4ba1-af59-b5e6760a4cdf'
    publish_iteration_name = 'Iteration2'
    url="https://treasureblob.blob.core.windows.net/treasurecontainer/"+photo
    imgFile="utility/custom_vision/pic/sample.jpg"
    print(url)
    urllib.request.urlretrieve(url, imgFile)

    # 預測
    with open(imgFile, 'rb') as image_contents:
        results = predictor.classify_image(PROJECT_ID, publish_iteration_name, image_contents.read())

        # 顯示結果
        def result():
            for prediction in results.predictions:
                if prediction.tag_name=="Glass":
                    return("a")
                elif prediction.tag_name=="Plastic":
                    return("b")
                elif prediction.tag_name=="PC":
                    return("c")
                elif prediction.tag_name=="IA":
                    return("d")
                elif prediction.tag_name=="Battery":
                    return("f")
                else:
                    return("e")
                
    end=time.time()
    total=end-start
    
    print(total)
    datastore(result(), imgFile, url)

    #responsersult(result())
    # scrollresult(result())
