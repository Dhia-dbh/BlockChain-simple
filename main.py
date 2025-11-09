import hashlib
from datetime import datetime

class Block:
   def __init__(self, index, transaction, previousHash, difficulty):
         self.index = index
         self.transaction = transaction
         self.previousHash = previousHash
         self.difficulty = difficulty
         self.timestamp = datetime.now()
         
   def hashBlock(self):
      data = f"{self.index}{self.transaction}{self.previousHash}{self.timestamp}"
      return hashlib.sha256(data.encode()).hexdigest()
         
class BlockChain:
   def __init__(self, difficulty=4):
      self.index = 0
      self.difficulty = difficulty
      self.chain = [Block(self.index, "Genesis Block", "0"*64, self.difficulty)]
      
   def addBlock(self, transaction):
      self.index += 1
      newBlock = Block(self.index, transaction, self.getLastBlock().hashBlock(), self.difficulty)
      self.chain.append(newBlock)
      
      
   def getLastBlock(self):
      return self.chain[-1]
   
   
if __name__ == "__main__":
   blockchain = BlockChain()
   blockchain.addBlock("Alice sends 5 BTC to Bob")
   blockchain.addBlock("Bob sends 2 BTC to Charlie")
   blockchain.addBlock("Charlie sends 1 BTC to David")
   
   for block in blockchain.chain:
      print(f"Block {block.index} Hash: {block.hashBlock()}")