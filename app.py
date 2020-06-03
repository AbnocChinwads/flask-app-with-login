import os
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getrandom(16)


@app.route("/", methods=["GET", "POST"])
def index():
    """if request.method == "POST":"""
    return render_template("index.html", page_title="Index")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
