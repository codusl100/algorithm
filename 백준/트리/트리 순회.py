N = int(input())

graph = {}
for _ in range(N):
	a, b, c = map(str, input().split())
	graph[a] = [b, c]


def preorder(node):
	if node != '.':
		print(node, end = "")
		preorder(graph[node][0])
		preorder(graph[node][1])
		
def inorder(node):
	if node != '.':
		inorder(graph[node][0])
		print(node, end = "")
		inorder(graph[node][1])
		
def postorder(node):
	if node != '.':
		postorder(graph[node][0])
		postorder(graph[node][1])
		print(node, end = "")
		

preorder('A')
print()
inorder('A')
print()
postorder('A')