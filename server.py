from flask import Flask, render_template, url_for, redirect
from flask import request, jsonify, send_file
import time
app = Flask(__name__)
tcp_dump = False
filename = None

@app.route('/tcp_flag', methods=['GET', 'POST'])
def tcp_flag():
    global tcp_dump
    if request.method == "GET":
        return jsonify({"tcp_flag": tcp_dump})
    elif request.method == "POST":
        tcp_dump = False
        return jsonify({"tcp_flag": tcp_dump})


@app.route("/", methods=['GET', 'POST'])
def start_dumping():
    global tcp_dump, filename
    if request.method == 'GET':
        return render_template('start_dumping.html')
    else:
        # ans = request.form.keys()
        # if ans[0] == 'start':
        tcp_dump = True
        filename = str(int(time.time()))
        return redirect(url_for('stop_dumping'))

@app.route("/stop_dumping", methods=['GET', 'POST'])
def stop_dumping():
    global tcp_dump, filename
    if request.method == 'GET':
        return render_template('stop_dumping.html')
    else:
        tcp_dump = False
        return redirect(url_for('download', file_id=filename))

@app.route("/download/<file_id>", methods=['GET'])
def download(file_id):
    return render_template('download.html')

@app.route("/filename", methods=['GET'])
def get_filename():
    global filename
    return jsonify({"filename": filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
