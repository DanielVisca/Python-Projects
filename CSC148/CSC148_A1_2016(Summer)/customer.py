class Customer:
    """A Customer.
 
    This class represents a customer in the simulation. Each customer will
    enter the simulation at _entry_time, will wait at most _patience turns.
    The restaurant need _prepare_time turns to prepare this customer order,
    and will receive _profit if can serve this customer on time.
 
    Your main task is to implement the remaining methods.
 
    === Private Attributes ===
    :param _entry_turn:Turn that customer enters restaurant
    :type _entry_turn:
    :param id: A unique id that is used to easily identify that customer.
    :type id:
    :param _prepare_time: Time it takes to prepare order for customer
    :type _prepare_time:
    :param _profit: Profit made when customer's order is prepared
    :type _profit:
    :param _patience: The number of turns this customer will wait
    :type _patience:
    """
 
    def __init__(self, information):
        """Initialize new Customer defined by order time, profit, patience and 
           id.
 
        :param information: The customer's information
        :type: str
        :rtype: None
        """
 
        tmp = information.split("\t")
        self._entry_turn = int(tmp[0].strip())
        self.id = int(tmp[1].strip())
        self._profit = float(eval("%.2f" % float(tmp[2].strip())))
        self._prepare_time = int(tmp[3].strip())
        self._patience = int(tmp[4].strip())
 
    def entry_turn(self):
        """Return the turn number for this customer
 
        :param self: This customer
        :type self: Customer
        :rtype: int
 
        >>> a = Customer('1	34643	5	6	7')
        >>> a.entry_turn()
        1
        """
        return self._entry_turn
 
    def id(self):
        """Return a unique id that is used to identify this customer
 
        :param self: This customer
        :type self: Customer
        :rtype: int
 
        >>> a = Customer('1	34643	5	6	7')
        >>> a.id()
        34643
        """
        return self.id
 
    def profit(self):
        """Return the profit made from this customer
 
        :param self: This customer
        :type self: Customer
        :rtype: int
 
        >>> a = Customer('1	34643	5	6	7')
        >>> a.profit()
        5
        """
        return self._profit
 
    def prepare_time(self):
        """Return the prepare time for this customer's order
 
        :param self: This customer
        :type self: Customer
        :rtype: int
 
        >>> a = Customer('1	34643	5	6	7')
        >>> a.prepare_time()
        6
        """
        return self._prepare_time
 
    def patience(self):
        """Return the amount of turns this customer is patient for
 
        :param self: This customer
        :type self: Customer
        :rtype: int
 
        >>> a = Customer('1	34643	5	6	7')
        >>> a.patience()
        7
        """
        return self._patience
 
    def __eq__(self, other):
        """
        Determine whether one customer has the same parameters as another.
        :param self: This customer
        :type self: Customer
        :param other: Other customer
        :type other: Customer
        :rtype: bool
 
        >>> a = Customer('1	34643	5	6	7')
        >>> b = Customer('2	34643	5	6	7')
        >>> a == b
        False
        >>> a = Customer('1	34643	5	6	7')
        >>> c = Customer('1	34643	5	6	7')
        >>> a == c
        True
        """
        if type(self) != type(other):
            return False
 
        if self.id != other.id:
            return False
        if self._entry_turn != other._entry_turn:
            return False
        if self._profit != other._profit:
            return False
        if self._prepare_time != other._prepare_time:
            return False
        if self._patience != other._patience:
            return False
        return True
 

    def __str__(self):
        """
         Create a str representation of customer
        :param self: this customer
        :type self: Customer
        :rtype: str
 
        >>> a = Customer('1	34643	5	6	7')
        >>> print(a)
        '1	34643	5	6	7'
        """
 
        a = str(self._entry_turn) + "\t" + str(self.id) + "\t" + \
        str(self._profit) + "\t" + str(self._prepare_time) + "\t" + \
        str(self._patience)
 
        return a
    