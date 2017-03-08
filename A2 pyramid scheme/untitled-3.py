class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children

        :param value: value contained in this tree
        :type value: object
        :param children: possibly-empty list of children
        :type children: list[Tree]
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        :rtype: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other):
        """
        Return whether this Tree is equivalent to other.

        :param other: object to compare to self
        :type other: object}Tree
        :rtype: bool

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0):
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        :param indent: amount to indent each level of tree
        :type indent: int
        :rtype: str

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])
    

    def __contains__(self, v):
        """
        Return whether Tree self contains v.

        :param v: value to search this tree for
        :type v: object

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(5)
        True
        >>> t.__contains__(18)
        False
        """
        if len(self.children) == 0:
            # self is a leaf
            return self.value == v
        else:
            # self is not a leaf
            return self.value == v or any([v in x for x in self.children])


def leaf_count(t):
    """
    Return the number of leaves in Tree t.

    :param t: tree to count the leaves of
    :type t: Tree
    :rtype: int

    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> leaf_count(t)
    6
    """
    if len(t.children) == 0:
        # t is a leaf
        return 1
    else:
        # t is an internal node
        return sum([leaf_count(c) for c in t.children])
class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """

    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data and children left and right.

        @param BinaryTree self: this binary tree
        @param object data: data of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        @param BinaryTree self: this binary tree
        @param Any other: object to check equivalence to self
        @rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @param BinaryTree self: this binary tree
        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.data)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> BinaryTree(5, BinaryTree(6, BinaryTree(8), BinaryTree(9)), BinaryTree(10, BinaryTree(12), BinaryTree(7))).__contains__(7)
        True
        """
        return (self.data == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))
    
    
    def evaluate(b):
        """
        Evaluate the expression rooted at b.  If b is a leaf,
        return its float data.  Otherwise, evaluate b.left and
        b.right and combine them with b.data.
    
        Assume:  -- b is a non-empty binary tree
                 -- interior nodes contain data in {"+", "-", "*", "/"}
                 -- interior nodes always have two children
                 -- leaves contain float data
    
         @param BinaryTree b: binary tree representing arithmetic expression
         @rtype: float
    
        >>> b = BinaryTree(3.0)
        >>> evaluate(b)
        3.0
        >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
        >>> evaluate(b)
        12.0
        """
        if b.left is None and b.right is None:
            return b.data
        else:
            return eval(str(evaluate(b.left)) +
                        str(b.data) +
                        str(evaluate(b.right)))
    
    
    def postorder_visit(t, act):
        """
        Visit BinaryTree t in postorder and act on nodes as you visit.
    
        @param BinaryTree|None t: binary tree to visit
        @param (BinaryTree)->Any act: function to use on nodes
        @rtype: None
    
        >>> b = BinaryTree(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> def f(node): print(node.data)
        >>> postorder_visit(b, f)
        2
        6
        4
        10
        14
        12
        8
        """
        if t is None:
            pass
        else:
            postorder_visit(t.left, act)
            postorder_visit(t.right, act)
            act(t)
    
    
    def inorder_visit(root, act):
        """
        Visit each node of binary tree rooted at root in order and act.
    
        @param BinaryTree root: binary tree to visit
        @param (BinaryTree)->object act: function to execute on visit
        @rtype: None
    
        >>> b = BinaryTree(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> def f(node): print(node.data)
        >>> inorder_visit(b, f)
        2
        4
        6
        8
        10
        12
        14
        """
        if root is None:
            pass
        else:
            inorder_visit(root.left, act)
            act(root)
            inorder_visit(root.right, act)
    
    
    def visit_level(t, n, act):
        """
        Visit each node of BinaryTree t at level n and act on it.  Return
        the number of nodes visited visited.
    
        @param BinaryTree|None t: binary tree to visit
        @param int n: level to visit
        @param (BinaryTree)->Any act: function to execute on nodes at level n
        @rtype: int
    
        >>> b = BinaryTree(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> def f(node): print(node.data)
        >>> visit_level(b, 2, f)
        2
        6
        10
        14
        4
        """
        if t is None:
            return 0
        elif n == 0:
            act(t)
            return 1
        elif n > 0:
            return (visit_level(t.left, n-1, act) +
                    visit_level(t.right, n-1, act))
        else:
            return 0
    
    
    def levelorder_visit(t, act):
        """
        Visit BinaryTree t in level order and act on each node.
    
        @param BinaryTree|None t: binary tree to visit
        @param (BinaryTree)->Any act: function to use during visit
        @rtype: None
    
        >>> b = BinaryTree(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> print(b)
                14
            12
                10
        8
                6
            4
                2
        <BLANKLINE>
        >>> def f(node): print(node.data)
        >>> levelorder_visit(b, f)
        8
        4
        12
        2
        6
        10
        14
        """
        # this approach uses iterative deepening
        visited, n = visit_level(t, 0, act), 0
        while visited > 0:
            n += 1
            visited = visit_level(t, n, act)
    
    
    # assume binary search tree order property
    def bst_contains(node, value):
        """
        Return whether tree rooted at node contains value.
    
        Assume node is the root of a Binary Search Tree
    
        @param BinaryTree|None node: node of a Binary Search Tree
        @param object value: value to search for
        @rtype: bool
    
        >>> bst_contains(None, 5)
        False
        >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
        True
        """
        if node is None:
            return False
        elif value < node.data:
            return bst_contains(node.left, value)
        elif value > node.data:
            return bst_contains(node.right, value)
        else:
            return True
    
    
    def insert(node, data):
        """
        Insert data in BST rooted at node if necessary, and return new root.
    
        Assume node is the root of a Binary Search Tree.
    
        @param BinaryTree node: root of a binary search tree.
        @param object data: data to insert into BST, if necessary.
    
        >>> b = BinaryTree(5)
        >>> b = insert(b, 3)
        >>> b = insert(b, 12)
        >>> b = insert(b, 7)
        >>> print(b)
            12
                7
        5
            3
        <BLANKLINE>
        """
        return_node = node
        if not node:
            return_node = BinaryTree(data)
        elif data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
        else:  # nothing to do
            pass
        return return_node
    
    
    def swap(node):
        """
        Remove data in BST rooted at node if necessary, and return new root.
    
        Assume node is the root of a Binary Search Tree.
    
        @param BinaryTree node: root of a binary search tree.
        @rtype: None
    
        >>> b = BinaryTree(8)
        >>> b = insert(b, 5)
        >>> b = insert(b, 12)
        >>> b = insert(b, 1)
        >>> b = insert(b, 6)
        >>> b = insert(b, 9)
        >>> b = insert(b, 14)
        >>> print(b)
                14
            12
                9
        8
                6
            5
                1
        <BLANKLINE>
        >>> print(swap(b))
                1
            5
                6
        8
                9
            12
                14
        <BLANKLINE>
        """
        if node is None:
            return
        else:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            swap(node.left)
            swap(node.right)
        return node


def delete(node, data):
    """
    Remove data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param BinaryTree node: root of a binary search tree.
    @param object data: data to remove from BST, if necessary.
    """

    # get node containing data
    subtree, parent = lookup(node, data)

    if subtree is not None:
        child_count = children_count(subtree)

        if child_count == 0:
            # if node has no children, just remove it
            if parent:
                if parent.left is subtree:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node.data = None

        elif child_count == 1:
            # if node has 1 child
            # replace node with its child
            if subtree.left:
                n = subtree.left
            else:
                n = subtree.right
            if parent:
                if parent.left is subtree:
                    parent.left = n
                else:
                    parent.right = n
            else:
                node.left = n.left
                node.right = n.right
                node.data = n.data

        else:
            # if node has 2 children
            # find its successor
            parent = subtree
            successor = subtree.right
        #good till here
            extra = subtree.left
            subtree.data = successor.data 
            
            left_most = successor.left
            while left_most:
                parent = left_most.parent #?
                left_most = successor.left            
          # #  while successor.left:
             # #   parent = successor
                # #successor = successor.left
            left_most = extra
            # replace node data by its successor data
            
            subtree.data = successor.data
            # fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
                
                

def node_at_height(tree,node,height):
    if not tree:
        return False
    
    if height == 1:
        if tree.data == node:
            return True
        else:
            return False
        
    if not tree.left and not tree.right:
        return False        
    
    else:
        return any([node_at_height(tree.left,node, height - 1), node_at_height(tree.right,node, height - 1)])
    
    
def concactenate(t1,t2):
    if t2.left == None:
        t2.left = t1
    else:
        concactenate(t1,t2.left)
        
def mirror(t):
    if t.children:
        for i in range(len(t.children)//2):
            save = t.children[i]
            t.children[i] = t.children[-i-1]
            t.children[-i-1] = save
        for x in t.children:
            mirror(x)
            
            
    #//2 needs to be moved over a bracket
    #eval only works on strings
#1 big 0, 2 delete, 3 concatenate, 4 mirror 5 tree inside tree         ,6 doubly linked list,7 stacks
def in_tree(t1,t2):
    if t1.data == None:
        return True
    if not t2.data:
        return False
    if t1.data ==t2.data:
        if t1.left and t2.right:
            return all([in_tree(t1.left,t2.left),in_tree(t1.right,t2.right)])
        
        if t1.left:
            in_tree(t1.left,t2.left)
        elif t1.right:
            in_tree(t1.right, t2.right)
        else:
            return True
    else:
        return any([in_tree(t1,t2.left),in_tree(t1,t2.right)])
                    
t2 = BinaryTree(1,BinaryTree(2,BinaryTree(3)),BinaryTree(4,BinaryTree(5),BinaryTree(6)))
t1 = BinaryTree(2,BinaryTree(3))
in_tree(t1,t2)