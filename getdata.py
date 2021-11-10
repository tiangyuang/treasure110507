from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time
import urllib.request
# from flask import Flask
class getdata:
    def __init__(self,result):
        self.result=result
        
    start=time.time()

    # 傳入prediction-key及endpoint
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": '2f526f1de6384a51b6db8de11c8e44d8'})
    predictor = CustomVisionPredictionClient(endpoint='https://westus2.api.cognitive.microsoft.com/', credentials=credentials)

    # 設定project.id, publish_iteration_name, 圖片位置及名稱
    PROJECT_ID = 'bc1eede9-2056-44bc-afa1-4aafc69fab3c'
    publish_iteration_name = 'Iteration1'
    url="https://treasureblob.blob.core.windows.net/treasurecontainer/d5.jpg"
    imgFile="D:/Treasure110507/picture-testing/sample.jpg"
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

    def test():
        print("i'm test")