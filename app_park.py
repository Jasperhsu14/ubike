from flask import Flask, render_template
import urllib.request as request
import json

app = Flask(__name__)


def get_data():
    src = "https://opengov.tainan.gov.tw/OpenApi/api/service/Get/c3604e1d-c4e1-4224-9d41-084ce299c3bf"
    with request.urlopen(src) as response:
        data = json.load(response)
    return data


@app.route('/')
def index():
    data = get_data()
    return render_template('parking_list.html', data=data)


if __name__ == '__main__':
    app.run()
