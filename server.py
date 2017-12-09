from flask import Flask, render_template
from flask import request
import sys, os
from threading import Timer

app = Flask(__name__)

@app.route("/redirect", methods=['GET'])
def redirect():
    with open('test', 'w') as f:
        f.write("10")
    return render_template('redirect.html')

@app.route("/dumping", methods=['GET'])
def dumping_data():
    return render_template('dumping.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print "elo"
    app.run(host='0.0.0.0', port=5050)
