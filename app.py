from flask import Flask, render_template
import urllib.request as request
import json


src = "https://opengov.tainan.gov.tw/OpenApi/api/service/Get/c3604e1d-c4e1-4224-9d41-084ce299c3bf"
# src = "https://parkweb.tainan.gov.tw/api/parking.php"
with request.urlopen(src) as response:
    data = json.load(response)
    # print(data["data"])

    for parking in data["data"]:
        print(parking["name"])

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('parking_list.html', data=data)


if __name__ == '__main__':
    app.run()
