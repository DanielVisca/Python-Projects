
 
#if file is None.. create instance

from collections import deque
class Network(object):
    """A pyramid network.

    This class represents a pyramid network. The network topology can be loaded
    from a file, and it can find the best arrest scenario to maximize the seized
    asset.

    You may, if you wish, change the API of this class to add extra public
    methods or attributes. Make sure that you do not change the public methods
    that were defined in the handout. Otherwise, you may fail test results for
    those methods.

    """

    # === Attributes ===
    # TODO: Complete this part

    def __init__(self, member_name=None):
        """
        Create Network self with content member_name

        :param member_name: member_name contained in this tree
        :type member_name: object
        """
        self.member_name = member_name
        self.list_of_arrest = []
        
    def load_log(self, log_file_name):
        """Load the network topology from the log log_file_name.
        
        @type self: Network
        @type log_file_name: file    #param or type?
        @rtype: None
        """

        #open file
        file = open(log_file_name, 'r')
    
        #list consists of each line from file  
        self.list_of_lines = []   
        for line in file:
            line.strip()
            self.list_of_lines.append(line)
        
        #--Create Network--
        #if big boss, assign name
        if self.member_name == None:
            self.member_name = get_member(self.list_of_lines[0])
            
        
        self.tree = self.create_tree(self.member_name)
        
        
    
    def create_tree(self, member_name):
        """Return a Tree from member name
        
        @type member_name: str
        @rtype: Tree
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.create_tree('Liam')
        Tree('Liam', [Tree('Emma', [Tree('Mason'), Tree('Sophia'),
        Tree('Olivia')]), Tree('Jacob', [Tree('William', [Tree('James', 
        [Tree('Alexander')])]), Tree('Ethan')])])
        """
        if self.children == []:
            return Tree(member_name)
        else:
            return Tree(member_name, [self.create_tree(x) \
                                      for x in self.get_children(member_name)])    
    

    
    def sponsor(self, member_name):
        """Return the sponsor name of member with name member_name.

        @type member_name: str
        @rtype: str
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.sponsor('Emma')
        'Liam'
        """

        #searchers through the list of lines until members name is found. 
        #returns sponsor
        for line in self.list_of_lines:
            if get_member(line) == member_name:
                sponsor = get_sponsor(line)
                
                #The great boss's sponsor is string None as said in forum
                if sponsor == '':
                    return 'None'
                
                else:
                    return sponsor
                
            
    def mentor(self, member_name):
        """Return the mentor name of member with name member_name.

        @type member_name: str
        @rtype: str
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.mentor('Sophia')
        'Mason'
        """
#return 'None' for great boss
        sponsor = self.sponsor(member_name)
        siblings = self.get_children(sponsor) #and self
        mentor = 'None'
        
        #loop through siblings
        for sib in siblings:
            #if a sibling is at an earlier index, that sibling becomes their mentor
            #the sibling with the closest smaller index becomes the mentor when loop is done
            if siblings.index(sib) < siblings.index(member_name):
                mentor = sib
        
        #if no older siblings
        if mentor == 'None':
            #mentor is the sponsot
            mentor = sponsor
            
        return mentor
            
                
    #check if this returns the right sibling            
        
            


    def assets(self, member_name):
        """Return the assets of member with name member_name.

        @type member_name: str
        @rtype: int
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.assets('Alexander')
        60
        """
        #untested
        for line in self.list_of_lines:
            if get_member(line) == member_name:
                return get_assets(line)


    def children(self, member_name):
        """Return the name of all children of member with name member_name.
        
        @type member_name: str
        @rtype: list of str
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.children('Liam')
        ['Emma','Jacob']
        """
        list_ = []
        for line in self.list_of_lines:
            if get_sponsor(line) == member_name:
                list_.append(get_member(line))
        return list_
#TO BE WORKED ON
    
    def best_arrest_assets(self, maximum_arrest):
        """
        Search for the amount of seized assets in the best arrest scenario
        that maximizes the seized assets. Consider all members as target zero.

        @type maximum_arrest: int
        @rType: int
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.best_arrest_assets(4)
        162
        """
        
        #the arrest order with max profit
        max_ = 0
        #fill list with possible arrests
        arrest_list = []
        
        #create a list of all possible members
        list_of_names = []
        for line in self.list_of_lines:
            list_of_names.append(get_member(line))
        
                
              
         #I want a list of all possible arrests starting from every name, with len no greater than maximum arrest   
        for name in list_of_names:        
            tree = self.create_tree(name)
            #good till here
            x = self.final_helper(tree,maximum_arrest)
            #good here
            
            for list_ in x:
                assets = 0
                for names in list_:
                    assets += self.assets(names)
                if assets > max_:
                    max_ = assets

        return max_        
  
        
#TO BE WORKED ON
    def best_arrest_order(self, maximum_arrest):
        """Search for list of member names in the best arrest scenario that
        maximizes the seized assets. Consider all members as target zero,
        and the order in the list represents the order that members are
        arrested.

        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.best_arrest_order(4)
        ['Jacob','William','James','Alexander']
        """
        
        #the arrest order with max profit
        max_ = 0
        #fill list with possible arrests
        arrest_list = []
        
        #create a list of all possible members
        list_of_names = []
        for line in self.list_of_lines:
            list_of_names.append(get_member(line))
        
         
            
         #I want a list of all possible arrests starting from every name with len no greater than maximum arrest   
        for name in list_of_names:        
            tree = self.create_tree(name)
            #good till here
            x = self.final_helper(tree,maximum_arrest)
            #good here
            
            for list_ in x:
                assets = 0
                temp_list = []
                for names in list_:
                    temp_list.append(names)
                    assets += self.assets(names)
                if assets > max_:
                    max_ = assets
                    arrest_list = temp_list
                
            
        return arrest_list     
        

            

    def get_children(self, member_name):
        """
        Return a list of the members children from the file
        
        @type member_name: str
        @rtype: list
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.get_children('Liam')
        ['Emma','Jacob']
        """
        list_ = []
        for line in self.list_of_lines:
            if get_sponsor(line) == member_name:
                list_.append(get_member(line))
        return list_
    
    def can_rat_out(self, member_name):
        """Return a list of people that member_name can rat out
    
        @type member_name: str
        @rtype list of str
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> N.can_rat_out('Emma')
        ['Liam','Mason','Sophia','Olivia']
        """
        list_ = []
        for child in self.children(member_name):
            list_.append(child)
        
        sponsor = self.sponsor(member_name)
        if sponsor != 'None':
            list_.append(sponsor)
            
        mentor = self.mentor(member_name)
        if mentor not in list_ and mentor != 'None':
            list_.append(mentor)
        return list_
    
    def path(self, member, max_arrest, arrest_list=[]):
        """
        """
        if len(arrest_list) == max_arrest:
            list_ = []
            return arrest_list + self.path( 
        else:
            list_ = []
            lis.append(member)
            return  self.path(x,max_arrest - 1, arrest_list) for x in self.can_rat_out(member)
        
#TO BE WORKED ON    
    def tree_paths(self, root):
        if not root.children:
            return [root.value]
        else:
            final = []
            for child in root.children:
                sub_paths = self.tree_paths(child)
                
                if isinstance(sub_paths,list) and len(sub_paths) == 1:
                    temp = [root.value] + sub_paths
                    final.append(temp)
                else:
                    for path in sub_paths:
                        
                        if isinstance(path,list):
                            temp = [root.value] + path
                            final.append(temp)
                    
                            
                        
                            
            #idea: if first index is a string, append it to the previous list
            return final
        
   

    def final_helper(self, tree, max_arrest=10000):
        """
        """
        list_ = []
        x = self.tree_paths(tree
                            )
        for i in range(len(x)-1):
            z = gather_lists(x[i])
            list_.append(z)
        
        #cut list at max
        for order in list_:
            if len(order) > max_arrest:
                for i in range( len(order) - max_arrest):
                    if len(list_) != 0:
                        list_.pop()
                
        return list_
                
    
#TO BE WORKED ON
    def find_leafs(self, tree):
        """Return a list of all leaves in the tree
        
        @type tree: Tree
        @rType: list of str
        
        >>> N = Network()
        >>> N.load_log('topology1.txt')
        >>> tree = N.create_tree(N.member_name)
        >>> find_leafs(tree)
        ['Mason','Sophia','Olivia','Alexander','Ethan']
        """
        if not tree.children:
            return tree.value
        else:
            #make these 1 list
            return [self.find_leafs(x) for x in tree.children]
        
        
 
#--Helper Functions
#TO BE WORKED ON
def gather_lists(list_):
    """
    Concatenate all the sublists of L and return the result.
    
    :param list_: list of lists to concatenate
    :type list_: list[list[object]]
    :rtype: list[object]
        
    >>> gather_lists([['Liam', ['Emma', 'Mason']], ['Liam', ['Emma', 'Sophia']], ['Liam', ['Emma', 'Olivia']], ['Liam', ['Jacob', ['William', ['James', 'Alexander']]]], ['Liam', ['Jacob', 'Ethan']]])
    [['Liam','Emma', 'Mason'], ['Liam','Emma', 'Sophia'], ['Liam','Emma', 'Olivia'],['Liam','Jacob','William', 'James', 'Alexander'], ['Liam','Jacob', 'Ethan']]
    """
    
    final_list = []
    for x in list_:
        if isinstance(x, list):
            temp_list = []
            temp_list = gather_lists(x)
            for y in temp_list:
                final_list.append(y)
        if isinstance(x, str):
            final_list.append(x)
    return final_list  
"""
gather_lists([['Liam', ['Emma', 'Mason']], ['Liam', ['Emma', 'Sophia']], ['Liam', ['Emma', 'Olivia']], ['Liam', ['Jacob', ['William', ['James', 'Alexander']]]], ['Liam', ['Jacob', 'Ethan']]])
        
"""          
        

def get_member(line):
    """Return the name of member from line
    load_log helper function
    
    @type line: str
    @rtype: str
    
    >>> get_member('Example#')
    'Example'
    """
    index = int(line.find('#'))
    return line[:index]

def get_sponsor(line):
    """Return the name of the sponsor
    load_log helper function

    @type line: str
    @rtype: str
    
    >>> get_sponsor('str#example#')
    'example'
    """
    index = int(line.find('#')) + 1
    return line[index: line.rfind('#')]

def get_assets(line):
    """Return the assets for the line
    load_log helper function
    
    @type line: str
    @rtype: int
    
    >>> get_assets('####69')
    69
    """
    index = int(line.rfind('#')) + 1
    return int(line[index:])


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




N = Network()
N.load_log('topology1.txt')
N.path('Liam',4)  #

if __name__ == "__main__":
    # A sample example of how to use a network object
    network = Network()
    network.load_log("topology1.txt")
    member_name = "Liam"
    print(member_name + "'s sponsor is " + network.sponsor(member_name))
    print(member_name + "'s mentor is " + network.mentor(member_name))
    print(member_name + "'s asset is " + str(network.assets(member_name)))
    print(member_name + "'s childrens are " + str(network.children(member_name)))
    maximum_arrest = 10
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests will seize " + str(network.best_arrest_assets(maximum_arrest)))
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests is: " + str(network.best_arrest_order(maximum_arrest)))
    
    
