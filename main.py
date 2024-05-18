from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/')

def hello_world():
    url = "https://asuratoon.com/eternally-regressing-knight-chapter-1/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img",class_="ts-main-image")
    imglist=[]
    for image in images:
        image_url = image["src"]
        imglist.append(image_url) 
        print(f"Image URL: {image_url}")

    return render_template('index.html',data=imglist)
if __name__ == '__main__':
    app.run()
