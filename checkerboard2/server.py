from flask import Flask, render_template
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", num=4, num2=4, color="red", color2="black")

@app.route("/4")
def four():
    return render_template("index.html", num=4, num2=2, color="red", color2="black")

@app.route("/<int:num>/<int:num2>")
def rand(num, num2):
    return render_template("index.html", num=int(num/2), num2=int(num2/2), color="red", color2="black")

@app.route("/<int:num>/<int:num2>/<color>/<color2>")
def color(num, num2, color, color2):
    return render_template("index.html", num=int(num/2), num2=int(num2/2), color=color, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)