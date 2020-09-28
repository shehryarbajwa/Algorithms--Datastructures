def boggle_board(board, words):
    #initialize Trie
    trie = Trie()
    for word in words:
        trie.add_word(word)
    #Final words need to be in a hash table to avoid array duplication
    final_words = {}
    visited = [[False for letter in row] for row in board]
    for row in range(len(board)):
        for col in range(len(board[col])):
            explore(row, col, board, visited, trie.root, final_words)
    return list(final_words.keys())

def explore(row, col, board, visited, trie_node, final_words):
    #If visited, return
    if visited[row][col]:
        return
    #Letter on specific row, col
    letter = board[row][col]
    #If letter not in root, return
    if letter not in trie_node:
        return
    #Visit the node
    visited[row][col] = True
    #Update the trie, go one level down
    trie_node = trie_node[letter]

    #If trie is at last level, we know we store the entire word at last level
    #Update key entry in final words
    if '*' in trie_node:
        final_words[trie_node['*']] = True
    neighbours = get_neighbours(row, col, board)
    for neighbour in neighbours:
        explore(neighbour[0], neighbour[1], board, visited, trie_node, final_words)
    #Unvisit and backtrack
    visited[row][col] = False

def get_neighbours(row, col, board):
    #Total of 8 neighbours
    neighbours = []
    #Diagonal up-left
    if row > 0 and col > 0:
        neighbours.append([row - 1, col - 1])
    #Diagonal up-right
    if row > 0 and col < len(board[0]) - 1:
        neighbours.append([row - 1, col + 1])
    #Diagonal down-left
    if row < len(board) - 1 and col > 0:
        neighbours.append([row + 1, col - 1])
    #Diagonal down-right
    if row < len(board) - 1 and col < len(board[0]) - 1:
        neighbours.append([row + 1, col + 1])
    #Move-Up
    if row > 0:
        neighbours.append([row - 1, col])
    #Move-Down
    if row < len(board) - 1:
        neighbours.append([row + 1, col])
    #Move-left
    if col > 0:
        neighbours.append([row, col - 1])
    #Move-right
    if col < len(board[0]) - 1:
        neighbours.append([row, col + 1])
    
    return neighbours    

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add_word(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word