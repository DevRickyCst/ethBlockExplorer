from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

web3 = Web3(
    Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{os.getenv("INFURA_ENDPOINT")}')
)


class eth:
    def get_block(self, id):
        block_info = vars(web3.eth.get_block(int(id)))
        return block_info

    def get_transaction(self, trx_hash):
        # 0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060
        transaction = vars(web3.eth.get_transaction(trx_hash))
        print(transaction['blockHash'])
        return transaction

    def get_last_20_blocks(self):
        last_block = web3.eth.block_number
        blocks = []
        for i in range(5):
            blocks.append(self.get_block(last_block - i))
        return blocks


def get_value(account):
    address = web3.to_checksum_address(account)
    w_balance = web3.eth.get_balance(address)
    return(web3.from_wei(w_balance, 'ether'))