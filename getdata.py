from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time
import urllib.request
from flask import Flask

from datastore import datastore

   
def getData(photo):     
    
    start=time.time()

    # 傳入prediction-key及endpoint
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": 'ae5d89cda9ab489487077626758c7c4b'})
    predictor = CustomVisionPredictionClient(endpoint='https://treasureprediction.cognitiveservices.azure.com/', credentials=credentials)

    # 設定project.id, publish_iteration_name, 圖片位置及名稱
    PROJECT_ID = '01b046a9-37fd-4ba1-af59-b5e6760a4cdf'
    publish_iteration_name = 'Iteration1'
    url="https://treasureblob.blob.core.windows.net/treasurecontainer/"+photo
    imgFile="./pic/sample.jpg"
    urllib.request.urlretrieve(url, imgFile)


    #-----------------------
    # 產生Flask物件
    #-----------------------
    # app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     return ('')

    # 預測
    with open(imgFile, 'rb') as image_contents:
        results = predictor.classify_image(PROJECT_ID, publish_iteration_name, image_contents.read())

        # 顯示結果
        def result():
            for prediction in results.predictions:
                if prediction.tag_name=="玻璃":
                    return("a")
                elif prediction.tag_name=="塑膠":
                    return("b")
                elif prediction.tag_name=="紙容器":
                    return("c")
                elif prediction.tag_name=="鐵鋁":
                    return("d")
                elif prediction.tag_name=="電池":
                    return("f")
                else:
                    return("e")
                
    end=time.time()
    total=end-start
    print(total)
    datastore(result(), imgFile, url)

