from flask import Flask, render_template
from flask import request, jsonify

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

@app.route("/start_dumping", methods=['GET', 'POST'])
def start_dumping():
    global tcp_dump
    if request.method == 'GET':
        return render_template('start_dumping.html')
    else:
        ans = request.form.keys()
        if ans[0] == 'start':
            tcp_dump = True
            return render_template('stop_dumping.html')

@app.route("/download", methods=['POST'])
def stop_dumping():
    global tcp_dump
    ans = request.form.keys()
    if ans[0] == 'stop':
        tcp_dump = False
        return render_template('download.html')

@app.route('/tcp_flag', methods=['GET', 'POST'])
def tcp_flag():
    global tcp_dump
    if request.method == "GET":
        return jsonify({"tcp_flag": tcp_dump})
    elif request.method == "POST":
        tcp_dump = False
        return jsonify({"tcp_flag": tcp_dump})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
