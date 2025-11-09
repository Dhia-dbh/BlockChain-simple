import hashlib
from datetime import datetime

class Block:
      def __init__(self, previous_hash: str, transaction: str):
         self.transaction : str = transaction
         self.previous_hash : str = previous_hash
         data: str = transaction + previous_hash + str(datetime.now())
         self.block_hash : str = hashlib.sha256(data.encode()).hexdigest()

bloc1= Block("0000", "Alice envoi 5 BTC à Bob")
bloc2= Block(bloc1.block_hash, "Bob envoi 2 BTC à Charlie")
bloc3 = Block(bloc2.block_hash, "Charlie envoi 1 BTC à David")

print("Bloc 1 Hash:", bloc1.block_hash)
print("Bloc 2 Hash:", bloc2.block_hash)
print("Bloc 3 Hash:", bloc3.block_hash)