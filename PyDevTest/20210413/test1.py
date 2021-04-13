from anytree import Node, RenderTree

b1 = {'type':10 , 'cal':100}
b2 = {'type':11 , 'cal':101}
b3 = {'type':12 , 'cal':102}
b4 = {'type':13 , 'cal':103}

root = Node('root',value='')

broot = Node('bread',parent=root,value='')
level_1_child_1 = Node('a', parent=broot,value=b1)
level_1_child_2 = Node('b', parent=broot,value=b2)
level_2_child_1 = Node('c', parent=broot,value=b3)
level_2_child_2 = Node('d', parent=broot,value=b4)




for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name,node.value ))
    
    