from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    default_date = datetime.today().strftime("%Y-%m-%d")
    return render_template("index.html", default_date=default_date)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
