from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "anything"

@app.route("/")
def home():
    if "count" not in session:
        session["count"] =1
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route("/two")
def count():
    if "count" in session:
        session["count"] += 2
    return render_template("index.html")

@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)