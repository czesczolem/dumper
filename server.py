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
        if tcp_dump:
            return render_template('error.html')
        else:
            timestamp = str(int(time.time()))
            filename = request.form['filename'] + "_" + timestamp
            tcp_dump = True
            return redirect(url_for('stop_dumping'))

@app.route("/stop_dumping", methods=['GET', 'POST'])
def stop_dumping():
    global tcp_dump, filename
    if request.method == 'GET':
        return render_template('stop_dumping.html')
    else:
        tcp_dump = False
        return redirect(url_for('download', filename=filename))

@app.route("/download/<filename>", methods=['GET', 'POST'])
def download(filename):
    if request.method == 'GET':
        return render_template('download.html')
    else:
        return redirect(url_for('get_file', filename=filename))

@app.route("/get_file/<filename>", methods=['GET'])
def get_file(filename):
    try:
        output = filename + '.pcap'
        return send_file(output,
                         mimetype='text/csv',
                         attachment_filename=output,
                         as_attachment=True)
    except Exception:
        return render_template('no_file.html')

@app.route("/filename", methods=['GET'])
def get_filename():
    global filename
    return jsonify({"filename": filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
