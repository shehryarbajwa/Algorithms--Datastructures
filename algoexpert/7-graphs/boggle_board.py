#Time Complexity
#O(nm*8^s + ws) time
#Space Complexity
#O(nm + ws) space
def boggleBoard(board, words):
    # Write your code here.
    trie = Trie()
	for word in words:
		trie.add(word)
	final_words = {}
	visited = [[False for letter in row] for row in board]
	for i in range(len(board)):
		for j in range(len(board[i])):
			explore(i, j, board, trie.root, visited, final_words)
	return list(final_words.keys())

def explore(i,j,board, trie_node, visited, final_words):
	if visited[i][j]:
		return
	letter = board[i][j]
	if letter not in trie_node:
		return
	visited[i][j] = True
	trie_node = trie_node[letter]
	if "*" in trie_node:
		final_words[trie_node["*"]] = True
	neighbours = get_neighbours(i, j, board)
	for neighbour in neighbours:
		explore(neighbour[0], neighbour[1], board, trie_node, visited, final_words)
	visited[i][j] = False
	
def get_neighbours(i,j,board):
	neighbours = []
	if i > 0 and j > 0:
		neighbours.append([i - 1, j - 1])
	if i > 0 and j < len(board[0]) - 1:
		neighbours.append([i - 1, j + 1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbours.append([i + 1, j + 1])
	if i < len(board) - 1 and j > 0:
		neighbours.append([i + 1, j - 1])
	if i > 0:
		neighbours.append([i - 1, j])
	if i < len(board) - 1:
		neighbours.append([i + 1, j])
	if j > 0:
		neighbours.append([i, j - 1])
	if j < len(board[0]) - 1:
		neighbours.append([i, j + 1])
	return neighbours

class Trie:
	def __init__(self):
		self.root = {}
		self.end_symbol = "*"
		
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.end_symbol] = word
		
