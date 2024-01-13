from flask import render_template
from flask import request
from src.eth import eth


def render_block_view(id):
    _eth = eth()

    id = request.args.get("id")
    if id != None:
        return render_template("block.html", blockInfo=_eth.get_block(id))
    else:
        return render_template("block.html", blocksInfo=_eth.get_last_20_blocks())
