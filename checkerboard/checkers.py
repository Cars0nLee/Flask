from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", num=4, num2=4)

@app.route("/<int:num>")
def four(num):
    return render_template("index.html", num=int(num/2), num2=2)

@app.route("/<int:fnum>/<int:lnum>")
def ten(fnum, lnum):
    return render_template("index2.html", num=int(fnum/2), num2=int(lnum/2))

if __name__ == "__main__":
    app.run(debug=True)