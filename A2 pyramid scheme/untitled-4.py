def dfs_rec(graph,start,path = []):
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs_rec(graph, edge,path)
    return path
graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
print (dfs_rec(graph,1))


def sort_recursive_helper(recursive_helper_output, list_ = []):
    """Return the List in sorted order, treat as a tree and return a list of all paths from root to leafs
    
    @type input: list of ints and lists
    @rType: list of lists of ints
    
    >>> input = [1]
    >>> list_all_paths(input)
    [[1]]
    
    >>> input = [1,[2,[3],[4]],[5,[6],[7]]]]
    >>> list_all_paths(input)
    [[1,2,3],[1,2,4],[1,5,6],[1,5,7]]
    """
    if len(recursive_helper_output) == 1:
        list_.append(recursive_helper_output[0])
        return list_   #[0]? #this returns the same list 
    else:
        #Problem is the list is copied for [[3],[4]] which it shoudnt
        
        copy = list_.copy()
        copy.append(recursive_helper_output[0])
      #  return [sort_recursive_helper(x, copy) for x in children_of_list(recursive_helper_output) ]
        list = []
        for x in children_of_list(recursive_helper_output):
            list.append(sort_recursive_helper(x, copy))
        return list
        
    
def children_of_list(list_):
    """Treat a list as if it were a tree and return the list of 'children'
    
    @type list_: list of str's and lists of str's
    @rtype: list of list of str
    
    >>> x = [1,[2],[3]]
    >>> children_of_list(x)
    [[2],[3]]
    """
    return_list = []
    for i in list_:
        if isinstance(i, list):
            return_list.append(i)
    return return_list
x = [1,[2,[3],[4]]]
sort_recursive_helper(x)














taken at 4:45
 #   def recursive_helper(self, tree, maximum_arrest, visited=['None'] ):
        """Return a list of all possible arrest_scenarios starting at root
        
        @type self: Network
        @type tree: Tree
        @type maximum_arrest: int
        @rtype: list of str or lists 
        """
        #if the arrest order is trapped of finished
        #(max arrests made) or (((if all of the children names are in visited) or (no children)) and (mentor in visited) and (sponsor in visited))
            
  #      if (len(visited) - 1 == maximum_arrest) or(((len(tree.children) == 0) or all([tree.x.value in visited for x in tree.children])) and self.mentor(tree.value) in visited and self.sponsor(tree.value) in visited):
            #what do I want to return in this instance?
   #         return tree.value  # suppose to be a list
        
        
    #    else:
     #       new_visited = visited.append(tree.value)
      #      return [tree.value ] + [self.recursive_helper(x, maximum_arrest - 1, new_visited) for x in (tree.children + [self.create_tree(self.mentor(tree.value))])] 
         

#def sort_recursive_helper(tree, list_ = []):
    """Return the List in sorted order, treat as a tree and return a list of all paths from root to leafs
    
    only deals with tree not mentor and sponsor
    @type input: list of ints and lists
    @rType: list of lists of ints
    """
 #   if not tree.children:
  #      list_.append(tree.value)
   #     return list_   
    #else:
        
      #  copy = list_.copy()    
     #   copy.append(tree.value)
        
       # return [sort_recursive_helper(x,copy) for x in tree.children]






self.b_a_o_helper(maximum_arrest - 1, x)








"""
def b_a_o_helper(self, maximum_arrest, member):
    Return a list of possible arrests starting from member
    
    if self.can_rat_out(member) == [] or maximum_arrest == 1: #or 0?
        return member
    else:
        list_ = [[member]]
        for x in self.can_rat_out(member): 
            #maybe do this for all?
            
            if list_[-1]: # # #
                #hesitant about -1, maybe the - len (members ratteed?
                copy = list_[0].copy()
                list_[-1].append(x)
                list_.append(copy)
                
                for inner_list in list_:
                    copy = inner_list.copy()
                    inner_list.append(x)
                    list_.append(copy)
            
        return list_
""" 
7:55am 


if not isinstance(list_, list):
    return list_
else:
    return [gather_lists(x) for x in list_]
