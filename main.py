from flask import Flask, render_template, session, request

from views.transactions import render_transaction_view
from views.blocks import render_block_view
from src.eths import get_value

app = Flask(__name__)

app.secret_key = b''

@app.route("/")
def home():
    try:
        value = get_value(session['account'])
        return render_template("base.html", page = 'home', value= value)
    except:
        return render_template("base.html", page = 'home')


@app.route("/block")
@app.route("/block/<id>")
def block(id=None):
    return render_block_view(id)


@app.route("/transaction")
@app.route("/transaction/<id>")
def transaction(id=None):
    return render_transaction_view(id)

@app.route("/dex")
def dex(id=None):
    return render_template("base.html", page = 'dex')


@app.route("/set-cookie", methods=['POST'])
def get_cookie():
    json = request.get_json()
    session['account'] = json['account']
    session['networkId']=json['networkId']
    return {
        "Value":'Account bien enregistrer dans la session Flask'
    }


@app.route("/delete-cookie", methods=['POST'])
def delete_cookie():
    del session['account']
    return {
        "Value":'Account bien supprimer de la session Flask'
    }
if __name__ == "__main__":
    app.run(debug=True)
