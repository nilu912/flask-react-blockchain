from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS # type: ignore
from blockchain import Blockchain, Transaction, Block

my_blockchain = Blockchain(difficulty=2)

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data=request.json
    if not all(key in data for key in ["sender", "receiver", "amount"]):
        return jsonify({"error": "Missing transaction data"}),404
    transaction = Transaction(data['sender'], data['receiver'], data['amount'])
    new_block = my_blockchain.add_block([transaction])

    return jsonify({
        "message": "Transaction added successfully",
        "block_index": new_block.index,
        "block_hash": new_block.hash,
        "previous_hash": new_block.previous_hash

    }),201
@app.route('/get-chain/', methods=['GET'])
def get_chain():
    chain_data=[]
    for block in my_blockchain.chain:
         chain_data.append({
            "index": block.index,
            "previous_hash": block.previous_hash,
            "transactions": [str(tx) for tx in block.transactions],
            "hash": block.hash
        })
    return jsonify({"length": len(my_blockchain.chain), "chain": chain_data}),200

@app.route('/validate-chain', methods=['GET'])
def validate_chain():
    is_valid = my_blockchain.is_chain_valid()
    return jsonify({"Valid": is_valid}),200

if __name__ == '__main__':
    app.run(debug=True)
