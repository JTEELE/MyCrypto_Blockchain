from web3 import Web3
conn = Web3.HTTPProvider('http://127.0.0.1:8545')
w3 = Web3(conn)
print(w3.eth.blockNumber)
print(w3.eth.getBalance('0xE70C802f533C6C79388E001B58689A75103052a6'))

ETH = 'eth'
BTC = 'btc'
BTCTEST = 'btc-test'