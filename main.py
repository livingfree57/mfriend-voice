from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='.')


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
