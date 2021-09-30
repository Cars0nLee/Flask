from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play")
def level():
    return render_template("level.html", num=3)

@app.route("/play/<int:num>")
def level_2(num):
    return render_template("level.html", num=num)

@app.route("/play/<int:num>/<color>")
def level_3(num, color):
    return render_template("level.html", num=num, color=color)



if __name__ == "__main__":
    app.run(debug=True)