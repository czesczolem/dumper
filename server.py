from flask import Flask, render_template
from flask import request, jsonify
import sys, os
from threading import Timer

app = Flask(__name__)
tcp_dump = False

@app.route("/", methods=['GET'])
def index():
    return  render_template('index.html')

@app.route("/redirect", methods=['GET'])
def redirect():
    global tcp_dump
    if tcp_dump:
        return "tcp dump in use, please try again in few minutes"
    else:
        tcp_dump = True
        return render_template('redirect.html')

@app.route("/dumping", methods=['GET'])
def dumping_data():
    return render_template('dumping.html')

@app.route('/tcp_flag', methods=['GET', 'POST'])
def tcp_flag():
    if request.method == "GET":
        return jsonify({"tcp_flag": tcp_dump})
    # elif request.method == "POST":
    #     tcp_dump

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
