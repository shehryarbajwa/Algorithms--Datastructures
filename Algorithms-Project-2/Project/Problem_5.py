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
        string += 'Previous Hash: ' + str(self.previous_hash) + '\n'
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

#Test case 1
chain.add('Block data: Verily')
# Block 1
# Data: Block data: Verily
# Time: 2019-11-12T19:41:17.436385
# Hash: 8d9497380f89cae1b77ec43c691fff9ca58f06780cfaf2f66eb73ef5317eda68
# Previous Hash: 44cb005ee2e65d9cc817b0a083579369fb6c24a4be728cb43fd9d4c3ca7f4c2e
chain.add('Block data: Waymo')
# Block 2
# Data: Block data: Waymo
# Time: 2019-11-12T19:41:17.436400
# Hash: aa851349c0d495987d5ba653f3a80103cbf9c1535a0f69f0a59758b41c1bef05
# Previous Hash: 8d9497380f89cae1b77ec43c691fff9ca58f06780cfaf2f66eb73ef5317eda68

chain.add('Block data: Calico')
# Block 3
# Data: Block data: Calico
# Time: 2019-11-12T19:41:17.436406
# Hash: 22a0580efebbcffa6e322c4c494eb1b1fec604e1ad18ee16c0b974a5e09c44c3
# Previous Hash: aa851349c0d495987d5ba653f3a80103cbf9c1535a0f69f0a59758b41c1bef05
print(chain)