class Node:

    def __init__(self, info,ID):

        self.left = None  #less than value
        self.right = None #greater than value
        self.id = ID
        self.info = info
        self.childrenID = None

    def print_tree(self,tree):
        if ( tree is not None):
            if (tree.childrenID is None):
                print("ID : " +str(tree.id)+ " , Class : "+tree.info)
            else:
                print("ID : " +str(tree.id)+ " , Info : "+tree.info+ " , Left Child ID: "+str(tree.childrenID[0])+" , Right Child ID: "+str(tree.childrenID[1]))
                self.print_tree(tree.left)
                self.print_tree(tree.right)
