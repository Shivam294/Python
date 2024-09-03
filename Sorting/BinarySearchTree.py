class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right= None

def insert(node, key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left = insert(node.left, key)
    elif key>node.key:
        node.right = insert(node.right, key)
    return node

def search(root, key):
    if root is None or root.key==key:
        return root
    if root.key<key:
        return search(root.right, key)
    return search(root.left, key)

if __name__ == '__main__':
    root = None
    n=int(input("Enter n:"))
    root = insert(root, int(input()))
    for i in range (n):
        insert(root, int(input()))
    key= int(input("Enter key to be found: "))
    if search(root, key) is None:
        print(key, "Not Found.")
    else:
        print(key, "Found!")