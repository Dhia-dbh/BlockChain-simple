import hashlib
from tqdm import tqdm

class Block:
   MAX_NOUNCE_SEARCH = 1000000
   def __init__(self, signature, sender, reciepiant, difficulty=2):
      self.signature = signature
      self.sender:str = sender
      self.reciepiant:str = reciepiant
      self.difficulty: int = difficulty
      self.nounce: int | None = None

   def _copyBlock(self) -> "Block":
      return Block(
         self.signature,
         self.sender,
         self.reciepiant,
         self.difficulty
      )
      
   def _getBlockData(self) -> str:
      return f"{self.signature}{self.sender}{self.reciepiant}{self.difficulty}"
   
   def _getFullBlockData(self, nounce: int) -> str:
      return f"{self._getBlockData()}{nounce}"

   def setNounce(self, nounce:int) -> None:
      if not self._isNounceValid(nounce):
         return
      self.nounce = nounce
   
   @staticmethod
   def _hashBlock(blockData:str) -> str:
      return hashlib.sha256(blockData.encode()).hexdigest()
   
   @staticmethod
   def _hashBlockTwice(blockData:str) -> str:
      return Block._hashBlock(Block._hashBlock(blockData))
      
   def _isNounceValid(self, nounce):
      blockData = self._getFullBlockData(nounce)
      hash = Block._hashBlockTwice(blockData)
      difficulyHash = "0" * (self.difficulty-1) + "1"
      if hash < difficulyHash:
         return True
      return False
   
   def mine(self) -> tuple[int, str] | tuple[None, None]:
      for nounce in  tqdm(range(self.MAX_NOUNCE_SEARCH)):
         if self._isNounceValid(nounce):
            return nounce, Block._hashBlockTwice(self._getFullBlockData(nounce))
      return None, None
   
   def isBlockMined(self) -> bool:
      return self.nounce is not None
   

class BlockChain():
   def __init__(self):
      self.chain = []
   
   def addBlock(self, block: Block) -> bool:
      if not block.isBlockMined():
         return False
      self.chain.append(block)
      return True
   def getLastBlock(self) -> Block | None:
      if len(self.chain) == 0:
         return None
      return self.chain[-1]
   
if __name__ == "__main__":
   block = Block("This is really me sending money. source: Trust me bro",
                 "Dhia",
                 "SOS_Tunisia", difficulty=5)
   nounce, hash = block.mine()
   if nounce is not None:
      block.setNounce(nounce)
      print(f"Mined Block with Nounce: {nounce}, Hash: {hash}")
   else:
      print("Failed to mine the block within the maximum nounce search limit.")