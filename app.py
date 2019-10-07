from flask import Flask, render_template, request, jsonify
import json


app = Flask(__name__)
with open('color.json') as f:
    color = json.load(f)["color"]


@app.route('/', methods=["GET"])
def render_html():
    return render_template("index.html")


@app.route('/color', methods=["POST"])
def change_color():
    color = request.data.decode('utf-8')
    print("post", color)
    with open('color.json', 'w') as f:
        json.dump({"color": color}, f)
    return "ok"


@app.route('/color', methods=["GET"])
def get_color():
    with open('color.json') as f:
        color = json.load(f)["color"]
    print('get', color)
    return color
    
    
if __name__ == '__main__':
    app.run(debug=True)