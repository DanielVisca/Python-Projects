

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

    def __init__(self, member_name=None, assets=0, children=[]):
        """
        Create Network self with content member_name, assets and 0 or more children

        :param value: value contained in this tree
        :type value: object
        :param children: possibly-empty list of children
        :type children: list[Tree]
        """
        self.member_name, self.assets = member_name, assets
        # copy children if not None
        self.children = children.copy() if children else []

        
    def load_log(self, log_file_name):
        """Load the network topology from the log log_file_name.
        
        @type self: Network
        @type log_file_name: file    #param or type?
        @rtype: None
        """

            
        """
        file = open(log_file_name, 'r')
        line = file.readline().strip()
        
        self.dict_of_members[get_member(line)] = {'sponsor: ':None, 'assets: ': get_assets(line)}
        line = file.readline().strip()
        while line != '':
            self.dict_of_members[get_member(line)] = {'sponsor: ':get_sponsor(line), 'assets: ': get_assets(line)}
            line = file.readline().strip()
        for name in self.dict_of_members:
            for other_name in self.dict_of_members:
                if self.dict_of_members[other_name]['sponsor: '] == name:
                    if 'children: ' in self.dict_of_members[name].keys():
                        self.dict_of_members[name]['children: '].append(other_name)
                    else:
                        self.dict_of_members[name]['children: '] = [other_name]
                        
        """
        
    def create_tree(self, member_name):
        """Return a Tree from member name
        @type member_name: str
        @rtype: Tree
        """
        if self.children == []:
            return Tree(member_name)
        else:
            return Tree(member_name, [self.create_tree(x) for x in self.get_children(member_name)])         
        
        


###########

    def recursive_helper(self, tree, maximum_arrest):
        if (maximum_arrest == 0) or len(tree.children) == 0:
            return self.assets(tree.value)
    
        else:
            return [self.assets(tree.value)] + [self.recursive_helper(x, maximum_arrest - 1) for x in tree.children]
        
        
        
        
        
        
        [20, [32, 14, 5, 8], [50, [42, [10, 60]], 5]]