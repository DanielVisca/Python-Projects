"""Danial hates Docstrings"""

class LinkedListNode:
    """
    Node to be used in linked list

    === Public Attributes ===
    :param LinkedListNode next_: successor to this LinkedListNode
    :param object value: data this LinkedListNode represents
    """

    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        :param value: data of this linked list node
        :type value: object
        :param next_: successor to this LinkedListNode.
        :type next_: LinkedListNode|None
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        :rtype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        s = "{} ->".format(self.value)
        cur_node = self
        while cur_node is not None:
            if cur_node.next_ is None:
                s += "|"
            else:
                s += " {} ->".format(cur_node.next_.value)
            cur_node = cur_node.next_
        return s

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        :param LinkedListNode self: this LinkedListNode
        :param LinkedListNode|object other: object to compare to self.
        :rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        self_node, other_node = self, other

        while (self_node is not None and
               type(self_node) is type(other_node) and
               self_node.value == other_node.value):
            self_node, other_node = self_node.next_, other_node.next_
        return self_node is None and other_node is None


class CircularLinkedList:
    """
    Circular collection of LinkedListNodes

    === Attributes ==
    :param: back: back node of this CircularLinkedList
    :type back: LinkedListNode
    """

    def __init__(self, value):
        """
        Create CircularLinkedList self with data value.

        :param value: data of the front element of this circular linked list
        :type value: object
        """
        self.back = LinkedListNode(value)
        #back.next_ corresponds to front
        self.back.next_ = self.back

    def __str__(self):
        """
        Return a human-friendly string representation of CircularLinkedList self
        :rtype: str

        >>> lnk = CircularLinkedList(12)
        >>> str(lnk)
        '12 ->'
        """

        #back.next_ corresponds to front
        current = self.back.next_
        result = "{} ->".format(current.value)
        current = current.next_
        while current is not self.back.next_:
            result += " {} ->".format(current.value)
            current = current.next_
        return result

    def append(self, value):
        """
        Insert value before LinkedList front, i.e self.back.next_.

        :param value: value for new LinkedList.front
        :type value: object
        :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> print(lnk)
        12 -> 99 -> 37 ->
        """
        self.back.next_ = LinkedListNode(value, self.back.next_)
        self.back = self.back.next_

    def reverse_print1(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print1(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print1(lnk.back)
        37
        """
        seen = []
        while current.next_ not in seen:
            seen.append(current.value)
            current = current.next_
        return current

    def reverse_print2(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print2(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print2(lnk.back)
        37
        """
        pass

    def reverse_print3(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print3(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print3(lnk.back)
        37
        """
    #    seen = []
#        while current.next_ not in seen:
 #           seen.append(current.value)
  #          current = current.next_
   #     return current

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


def list_internal(t):
    """
    Return list of values in internal nodes of t.

    :param t: tree to list internal values of
    :type t: Tree
    :rtype: list[object]

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if len(t.children) == 0:
        return []
    else:
        return [t.value] + gather_lists([list_internal(c) for c in t.children])


def arity(t):
    """
    Return the maximum branching factor (arity) of Tree t.

    :param t: tree to find the arity of
    :type t: Tree
    :rtype: int

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    return max([len(t.children)] + [arity(n) for n in t.children])

def is_full(t, n):
    """
    """
    if len(t.children) > n:
        return False
    if len(t.children) == 0:
        return True
    else:
        return (True not in [is_full(x,n) for x in t.children])
    
t = Tree(1,[Tree(2),Tree(3),Tree(4)])
t1 = Tree(1,[Tree(2),Tree(3,[Tree(4)])])
is_full(t,1)
# helper function that may be useful in the functions
# above
def gather_lists(list_):
    """
    Concatenate all the sublists of L and return the result.

    :param list_: list of lists to concatenate
    :type list_: list[list[object]]
    :rtype: list[object]

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list


# helpful helper function
def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    :param t: tree to populate from list_
    :type t: Tree
    :param list_: list of values to populate from
    :type list_: list
    :param arity: maximum branching factor
    :type arity: int
    :rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


def is_full(t, n):
    """
     Return whether tree t is full with respect to arity n

    :param t: a general tree
    :type t: Tree
    :param n: a given branching factor for the tree
    :type n: int
    :rtype: bool

    >>> t1 = descendants_from_list(Tree(0), [], 3)
    >>> is_full(t1, 3)
    True
    >>> t2 = descendants_from_list(Tree(0), [1, 2, 3], 3)
    >>> is_full(t2, 3)
    True
    >>> t3 = descendants_from_list(Tree(0), [1, 2, 3, 4], 3)
    >>> is_full(t3, 3)
    False
    >>> t4 = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6], 3)
    >>> is_full(t4, 3)
    True
    """
    # to be developed by you

    pass


def is_full1(t, n):
    """
     Return whether tree t is full with respect to arity n

    :param t: a general tree
    :type t: Tree
    :param n: a given branching factor for the tree
    :type n: int
    :rtype: bool

    >>> t1 = descendants_from_list(Tree(0), [], 3)
    >>> is_full1(t1, 3)
    True
    >>> t2 = descendants_from_list(Tree(0), [1, 2, 3], 3)
    >>> is_full1(t2, 3)
    True
    >>> t3 = descendants_from_list(Tree(0), [1, 2, 3, 4], 3)
    >>> is_full1(t3, 3)
    False
    >>> t4 = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6], 3)
    >>> is_full1(t4, 3)
    True
    """
    pass


def is_full2(t, n):
    """
     Return whether tree t is full with respect to arity n

    :param t: a general tree
    :type t: Tree
    :param n: a given branching factor for the tree
    :type n: int
    :rtype: bool

    >>> t1 = descendants_from_list(Tree(0), [], 3)
    >>> is_full2(t1, 3)
    True
    >>> t2 = descendants_from_list(Tree(0), [1, 2, 3], 3)
    >>> is_full2(t2, 3)
    True
    >>> t3 = descendants_from_list(Tree(0), [1, 2, 3, 4], 3)
    >>> is_full2(t3, 3)
    False
    >>> t4 = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6], 3)
    >>> is_full2(t4, 3)
    True
    """
    pass


def is_full3(t, n):
    """
     Return whether tree t is full with respect to arity n

    :param t: a general tree
    :type t: Tree
    :param n: a given branching factor for the tree
    :type n: int
    :rtype: bool

    >>> t1 = descendants_from_list(Tree(0), [], 3)
    >>> is_full3(t1, 3)
    True
    >>> t2 = descendants_from_list(Tree(0), [1, 2, 3], 3)
    >>> is_full3(t2, 3)
    True
    >>> t3 = descendants_from_list(Tree(0), [1, 2, 3, 4], 3)
    >>> is_full3(t3, 3)
    False
    >>> t4 = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6], 3)
    >>> is_full3(t4, 3)
    True
    """
    pass

            

def parenthesize(b):
    """
    Return a parenthesized expression equivalent to the arithmetic
    expression tree rooted at b.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    :param b: arithmetic expression tree
    :type b: BinaryTree
    :rtype: str

    >>> b1 = BinaryTree(3.0)
    >>> print(parenthesize(b1))
    3.0
    >>> b2 = BinaryTree(4.0)
    >>> b3 = BinaryTree(7.0)
    >>> b4 = BinaryTree("*", b1, b2)
    >>> b5 = BinaryTree("+", b4, b3)
    >>> print(parenthesize(b5))
    ((3.0 * 4.0) + 7.0)
    """
    if b.left is None and b.right is None:
        return str(b.data)
    else:
        return "({} {} {})".format(parenthesize(b.left),
                                   b.data,
                                   parenthesize(b.right))


def list_longest_path(node):
    """
    List the data in a longest path of node.

    :param node: tree to list longest path of
    :type node: BinaryTree|None
    :rtype: list[object]

    >>> list_longest_path(None) 
    []
    >>> list_longest_path(BinaryTree(5))
    [5]
    >>> b1 = BinaryTree(7)
    >>> b2 = BinaryTree(3, BinaryTree(2), None)
    >>> b3 = BinaryTree(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    if node is None:
        return []
    else:
        path_left = list_longest_path(node.left)
        path_right = list_longest_path(node.right)
        if len(path_right) > len(path_left):
            return [node.data] + path_right
        else:
            return [node.data] + path_left


def insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    :param node: root of a binary search tree.
    :type node: BinaryTree
    :param data: data to insert into BST, if necessary.
    :type data: object

    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
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


def max_value1(t):
    """
    Return the max value in BinaryTree t

    :param t: a not None binary tree
    :type t: BinaryTree
    :return: the maximum value in the tree
    :rtype: object

    >>> t1 = BinaryTree(8)
    >>> max_value1(t1)
    8
    >>> t2 = BinaryTree(8,BinaryTree(7,BinaryTree(12),BinaryTree(5)),BinaryTree(11))
    >>> max_value1(t2)
    12
    """
    pass


def max_value2(t):
    """
    Return the max value in BinaryTree t

    :param t: a not None binary tree
    :type t: BinaryTree
    :return: the maximum value in the tree
    :rtype: object

    >>> t1 = BinaryTree(8)
    >>> max_value2(t1)
    8
    >>> t2 = BinaryTree(8,BinaryTree(7,BinaryTree(12),BinaryTree(5)),BinaryTree(11))
    >>> max_value2(t2)
    12
    """
    pass


class Container:
    """
    a data structure to store and retrieve objects.

    This is an abstract class that is not meant to be instantiated itself,
    but rather subclasses are to be instantiated.
    """
    def __init__(self):
        """
        Create a new and empty Container self.
        """
        self._content = None
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def add(self, obj):
        """
        Add object obj to Container self.

        :param obj: object to place onto Container self
        :type obj: Any
        :rtype: None
        """
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def remove(self):
        """
        Remove and return an element from Container self.

        Assume that Container self is not empty.
        :return an object from Container slef
        :rtype: object
        """
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def is_empty(self):
        """
        Return whether Container self is empty.

        :rtype: bool
        """
        return len(self._content) == 0

    def __eq__(self, other):
        """
        Return whether Container self is equivalent to the other.

        :param other: a Container
        :type other: Container
        :rtype: bool
        """
        return type(self)== type(other) and self._content == other._content

    def __str__(self):
        """
        Return a human-friendly string representation of Container.

        :rtype: str
        """
        return str(self._content)


class Stack(Container):
    """
    Last-in, first-out (LIFO) stack.
    """
    def __init__(self):
        """
        Create a new, empty Stack self.

        Overrides Container.__init__

        """
        self._content = []

    def add(self, obj):
        """
        Add object obj to top of Stack self.

        Overrides Container.add

        :param obj: object to place on Stack
        :type obj: Any
        :rtype: None
        """
        self._content.append(obj)

    def remove(self):
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        Overrides Container.add

        :rtype: object
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._content.pop()

class Queue:
    ''' Represent a FIFO queue.
    '''

    def __init__(self):
        ''' (Queue) -> NoneType

        Create and initialize new queue self.
        '''
        self._data = []

    def add(self, o):
        ''' (Queue, object) -> NoneType

        Add o at the back of this queue.
        '''
        self._data.append(o)

    def remove(self):
        ''' (Queue) -> object

        Remove and return front object from self.

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        '''
        return self._data.pop(0)

    def is_empty(self):
        ''' (Queue) -> bool

        Return True queue self is empty, False otherwise.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        '''
        return self._data == []

