#Importing python Library that provides a SHA356 hashing function
import hashlib

#Creating the class that generates creates the base functionality of the blockchain
class simple_blockchain:
    #intilization function requires two parameters the previous block's hash
    # and the list of transactions to be added to the current block
    def __init__(self, previous_block_hash, transactions):
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions
        #defining the data of the block, must include the previous hash and current data
        self.data = "_".join(transactions) + " - "+ previous_block_hash
        # defining the hash for this block as the hash of the self.data
        self.block_hash = hashlib.sha256(self.data.encode()).hexdigest()

# Declaring the transactions 
t1,t2,t3,t4,t5,t6 = 'Transaction 1','Transaction 2','Transaction 3','Transaction 4','Transaction 5', 'Transaction 6'
#Creating the blocks
gen_block = simple_blockchain('Genesis Block',[t1,t2])
block_2 = simple_blockchain(gen_block.block_hash, [t3,t4])
block_3 = simple_blockchain(block_2.block_hash,[t5,t6])

#Printing the data to the console.
print('\nGenesis Block: \n',gen_block.data, gen_block.block_hash, '\n')
print('Block 2 : \n',block_2.data, block_2.block_hash,'\n')
print('Block 3 : \n', block_3.data,block_3.block_hash)

