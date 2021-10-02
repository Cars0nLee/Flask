from flask import Flask, render_template

app = Flask(__name__)



@app.route("/play/<int:num>/<color>")
def play(num, color):
    return render_template ("index.html", times=num, usercolor=color)




if __name__ == "__main__":
    app.run(debug=True)