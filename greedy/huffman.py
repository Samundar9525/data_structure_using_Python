# A Huffman Tree Node
class node:
	def __init__(self, freq, symbol, left=None, right=None):           # yahan default parametere ka use hua hai

		self.freq = freq

		self.symbol = symbol

		self.left = left

		self.right = right

		self.huff = ''


def printNodes(node, val=''):
	newVal = val + str(node.huff)

	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

	if(not node.left and not node.right):
		print(node.symbol," : ",newVal)

if __name__ == '__main__':


	chars = ['a', 'c', 'd', 'e', 'f','b']
	freq = [ 5, 12, 13, 16, 45,9]
	nodes = []

	for x in range(len(chars)):
		nodes.append(node(freq[x], chars[x]))

	while len(nodes) > 1:
		nodes = sorted(nodes, key=lambda x: x.freq)
		for i in range(len(nodes)):
			print(nodes[i].symbol, nodes[i].freq)
		print("-------------------------------")

		left = nodes[0]
		right = nodes[1]

		left.huff = 0
		right.huff = 1

		newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

		nodes.remove(left)
		nodes.remove(right)
		nodes.append(newNode)

	# Huffman Tree is ready!
	print(nodes[0].symbol,nodes[0].freq,nodes[0].huff)
	printNodes(nodes[0])
