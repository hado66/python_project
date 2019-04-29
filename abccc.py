import requests
import jsonpath

url='https://pg.qq.com/zlkdatasys/data_zlk_zlzx.json'
reponse=requests.get(url).json()
print(url)