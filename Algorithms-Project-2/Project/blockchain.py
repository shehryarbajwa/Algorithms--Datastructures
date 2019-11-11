import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        if self.previous_hash:
            sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        string = 'Data: ' + self.data + '\n'
        string += 'Time: ' + self.timestamp.isoformat() + '\n'
        string += 'Hash: ' + self.hash + '\n'
        return string

class Blockchain:

    def __init__(self):
        self.blocks = []
        first_block = Block(datetime.datetime.utcnow(), "Root", None)
        self.blocks.append(first_block)

    def add(self, data):
        block = Block(
            datetime.datetime.utcnow(),
            data,
            self.blocks[-1].hash
        )
        self.blocks.append(block)

    def get_block(self, index):
        return self.blocks[index]

    def size(self):
        return len(self.blocks)

    def __str__(self):
        string = ''
        for index, block in enumerate(self.blocks):
            string += 'Block ' + str(index) + '\n'
            string += str(block)
        return string
    
chain = Blockchain()
print(chain)

chain.add('Block data: Verily')
chain.add('Block data: Waymo')
chain.add('Block data: Calico')

print(chain)