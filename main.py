from flask import Flask, render_template, session, request

from src.eths import get_value, get_block, get_last_20_blocks, get_transaction

app = Flask(__name__)

app.secret_key = b'e3ba6fc7ec44173d32d96d251bc692db7182a5b36ea233f045c64c8ae270cdb2'

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
    id = request.args.get("id")
    if id != None:
        return render_template("base.html", page = 'block', blockInfo=get_block(id))
    else:
        return render_template("base.html", page = 'block', blocksInfo=get_last_20_blocks())


@app.route("/transaction")
@app.route("/transaction/<id>")
def transaction(id=None):
    id = request.args.get("id")
    if id:
        try:
            print(get_transaction( id))
            return render_template('base.html', page = 'transaction', transactionInfo=get_transaction(id))
        except:
            print('mauvais transaction hash')
            return render_template('base.html', page = 'transaction')
        
    else:
        print('ok')
        return render_template('base.html', page = 'transaction')

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
    del session['networkId']
    return {
        "Value":'Account bien supprimer de la session Flask'
    }
if __name__ == "__main__":
    app.run(debug=True)
