def NodeCreate(value, next):
    return [value, next]

def NodeValue(node):
    return node[0]

def NodeNext(node):
    return node[1]

def NodeSetValue(node, value):
    node[0] = value

def NodeSetNext(node, value):
    node[1] = next
    #return

def main():
    node1 = NodeCreate(15, None)
    print(node1)
    node2 = NodeCreate(12, node1)
    print(node2)
    print(NodeNext(node2))
    NodeSetValue(node1, 85)
    print(node1)

main()
