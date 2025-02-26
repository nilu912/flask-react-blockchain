import hashlib
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.amount}" 
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        tx_strings=str([str(tx) for tx in self.transactions])
        block_contents = (str(self.index)+tx_strings+str(self.previous_hash)+str(self.timestamp)+str(self.nonce))
        return hashlib.sha256(block_contents.encode()).hexdigest()
    def mine_block(self, difficulty):
        target='0'*difficulty
        while not self.hash.startswith(target):
            self.nonce+=1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined with hash: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
    def create_genesis_block(self):
        return Block(0, [Transaction("Genesis", "Network", 0)], "0")
    def get_latest_block(self):
        return self.chain[-1]
    def add_block(self, transactions):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), transactions, latest_block.hash)
        print(f"Mining Block {new_block.index}")
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if previous.hash != current.previous_hash:
                return False
        return True
if __name__ == "__main__":
    my_blockchain = Blockchain(difficulty=2)
    # print(my_block.chain[0].transactions[0])
    # print(my_block.get_latest_block())
    while(True):
        choice=input("Want to add block?<y/n>").lower()
        if choice!='y':
            print("See yaa Soon!")
            break
        sender=input("Enter Your Name: ").strip()
        receiver=input("Transact with: ").strip()
        try:
            amount=int(input("How much amount you want to transfer: "))
            if amount<0:
                print("Amount must be positive!")
                continue
        except:
            print("Invalid amount!")
            continue
        transaction = Transaction(sender,receiver,amount)
        new_block=my_blockchain.add_block([transaction])
        print("Your data Successfully added to the Blockcain: ")
        choice=input("Press 'Y' for verify.").lower()
        if(choice=='y'):
            print("Blockchain is Valid!" if my_blockchain.is_chain_valid() else "Blockchain is Corrupted!")
            for block in my_blockchain.chain:
                print(f"Block {block.index}")
                print(f"Previous Hash {block.previous_hash}")
                print(f"Transactions:")
                for tx in block.transactions:
                    print(f" {tx}")
                print(f"Hash {block.hash}")
                print(100*" ")