from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
color = '#ffffff'


@app.route('/', methods=["GET"])
def render_html():
    return render_template("index.html")


@app.route('/color', methods=["POST"])
def change_color():
    global color
    color = request.data.decode('utf-8')
    print("post", color)
    return "ok"


@app.route('/color', methods=["GET"])
def get_color():
    print('get', color)
    return color
    
    
if __name__ == '__main__':
    app.run(debug=True)