from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
color = '#ffffff'


@app.route('/', methods=["GET"])
def render_html():
    return render_template("index.html")


@app.route('/', methods=["POST"])
def change_color():
    global color
    color = request.form["color"]
    return render_template("index.html")


@app.route('/color', methods=["GET"])
def get_color():
    print(color)
    return color
    
    
if __name__ == '__main__':
    app.run(debug=True)