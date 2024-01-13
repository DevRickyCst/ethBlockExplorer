from flask import Flask
from flask import render_template

from views.transactions import render_transaction_view
from views.blocks import render_block_view


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/block")
@app.route("/block/<id>")
def block(id=None):
    return render_block_view(id)


@app.route("/transaction")
@app.route("/transaction/<id>")
def transaction(id=None):
    return render_transaction_view(id)


if __name__ == "__main__":
    app.run()
