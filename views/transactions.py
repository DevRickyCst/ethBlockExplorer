from flask import render_template
from flask import request

from src.eth import  eth


def render_transaction_view(id):
    _eth = eth()
    id = request.args.get("id")    

    if id:
        try:
            print(id)
            print(_eth.get_transaction( id))
            return render_template('transaction.html', transactionInfo=_eth.get_transaction(id))
        except:
            print('mauvais transaction hash')
            return render_template('transaction.html',)
        
    else:
        return render_template('transaction.html',)