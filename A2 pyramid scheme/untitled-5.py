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