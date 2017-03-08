from customer import Customer
class Restaurant(object):
    """A Restaurant.

    This class represents a restaurant in the simulation. This is the base
    class for different restaurant approaches. The main purpose of this
    class to define common interfaces for different approaches. If there
    are common tasks for all approaches that did not depend on a specific
    management style, they should be implemented here. Otherwise, they should
    be implemented in the subclasses.

    This class is abstract; subclasses must implement add_customer and
    process_turn functions.

    You may, if you wish, change the API of this class to add
    extra public methods or attributes. Make sure that anything
    you add makes sense for ALL approaches, and not just a particular
    approach.

    """

    # === Private Attributes ===
    # TODO: Complete this part

    def __init__(self):
        """Initialize a restaurant.
        """
        self._line_up = Deque()
        
        #Uncertain
        self._total_profit = 0
        self._total_customers = 0
        self._previous_customer = None
        self._total_customer_prepare_time = 1     
        self._name = ''        


    def add_customer(self, new_customer):
        """Add a new entering customer to the restaurant.

        :type new_customer: Customer
            The new customer that is entering the restaurant
        :rtype: None
        
        >>> c= MatApproach()
        >>> c.add_customer(Customer("1 34643 5 6 7"))
        >>> c.add_customer(Customer("3 44643 2 1 2"))
        >>> print(c._line_up[0])
        1 34643 5 6 7
        """
        self._line_up.add(new_customer)
    
    def process_turn(self, current_turn):
        """Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :type self: Restaurant
        :type current_turn: int
            The number of current turn
        :rtype: None
        """
        #1) see if restaurant is ready to serve a new customer
        if (self._total_customer_prepare_time == 1) or (self._previous_customer 
             and self._total_customer_prepare_time <= current_turn):
 
            #2) check if their are customers to be served
             #remove the current customer from the line up
            if not self._line_up.is_empty():
                current_customer = self._line_up.remove()
             #make  current customer ther previous customer
                self._previous_customer = current_customer
             
             #if the customers patience has not been used up       
                #check if the customer has waited longe than his patience allows. Example, arrived at 3 served at 8 and patience is 5 he will not be selected
                if (current_turn - 
                    current_customer.entry_turn()) \
                   < current_customer.patience():
                    self._total_profit += current_customer._profit
                    self._total_customers += 1
 
                    self._total_customer_prepare_time += \
                        current_customer.prepare_time()


    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the 
           report_file.
 
        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report
            into.
        :rtype: None
        
        >>> _name = 'Robin William'
        >>> _total_profit = 10
        >>> _total_customers = 100
        >>> file = open('report1', 'w')
        >>> write_report(file)
        >>> for line in file:
                print(line)
        Results for serving approach using Robin William's suggestion:
        Total profit: $10
        Customers served: 100
        """
#I am not certain about this docstring example

        report_file.write("Results for serving approach using {}'s suggestion:"\
                          .format(self._name))
        report_file.write("\n") 
        report_file.write('Total profit: ${}'.\
                          format(round(self._total_profit,2))) 
        report_file.write('\n') 
        report_file.write('Customer served: {}'.format(self._total_customers))
        report_file.write('\n')
    
        #TODO: Complete this part


class PatApproach(Restaurant):
    """A Restaurant with Pat management style.

    This class represents a restaurant that uses the Pat management style,
    in which customers are served based on their arrival time. This class is
    a subclass of Restaurant and implements two functions: add_customer and
    process_turn.

    """

    #TODO: Complete this part

#TODO: Complete this part
        
        
class PatApproach(Restaurant):
    """A Restaurant with Pat management style.
 
    This class represents a restaurant that uses the Pat management style,
    in which customers are served based on their arrival time. This class is
    a subclass of Restaurant and implements two functions: add_customer and
    process_turn.
 
    """
    def __init__(self):
        """Create an instance of PatApproach
        
        :param self: a restaurant
        :type: PatApproach
        :rtype: none
        Extend Restaurant
        """
        super(PatApproach, self).__init__()
        self._name ='Pat'
        

class MatApproach(Restaurant):
    """A Restaurant with Mat management style.
   
    This class represents a restuarant that uses the Mat management style, in
    which the last customer to arrive recieves their order first. This class is
    a subclass of Restaurant and implements ****___**** functions.
    """
    def __init__(self):
        """
        Create an instance of MatApproach
        
        :param self: a restaurant
        :type: MatApproach
        :rtype: none
        Extend Restaurant
        """
        super(MatApproach, self).__init__()
        #unnecessary but simpler for me right now
        self._line_up = Stack()
        self._name = 'Mat'
        
class MaxApproach(Restaurant):
    """A Restaurant with Max management style.
   
    This class represents a restuarant that uses the Max management style, in
    which the the customer is selected on who can bring the highest profit. 
    This class is
    a subclass of Restaurant
    """
    def __init__(self):
        """Initialize a restaurant with MaxApproach.
        
        :param self: a restaurant
        :type: MaxApproach
        :rtype: none
        """
        super(MaxApproach, self).__init__()
        #how do I add the priority for profit??
        self._line_up = Pqueue_profit()
        self._name = 'Max'

class PacApproach(Restaurant):
    """A Restaurant with Pac management style.
   
    This class represents a restuarant that uses the Pac management style, in
    which the customer who can be served in the shortest amount of time is 
    served first. This class is
    a subclass of Restaurant
    """
    
    def __init__(self):
        """Initialize a restaurant with PacApproach.
        
        :param self: a restaurant
        :type: PacApproach
        :rtype: none
        """
        super(PacApproach, self).__init__()  
        self._line_up = Pqueue_prepare_time()
        self._name = 'Pac'

    
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


class Queue(Container):
    """
    First in first out
    """
    
    def __init__(self):
        """
        Create an instance of Queue
        """
        self._content = []
       
    def add(self, obj):
        """
        Add an item to the Queue
       
        @type self: Queue
        @type obj: Any
        @rType: None
        """
        self._content.append(obj)
       
    def remove(self):
        """
        Remove and return top element of Stack self.
 
        Assume Stack self is not empty.
 
        :rtype: object
        >>> s = Queue()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        5
        """
        return self._content.pop(0)
   
    def is_empty(self):
        """
        Returns if Queue id empty
       
        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.add(1)
        >>> q.is_empty()
        False
        """
        return len(self._content) == 0
    
class Deque(Queue):
    
    def __init__(self):
        super(Deque, self).__init__()
        
    def add_to_front(self, obj):
        """
        Add the obj to the front of Deque self
       
        Extends class Queue. This is a new method.
        
        :param obj: object to add
        :type obj : object
        :rtype: None
        
        >>> d = Deque()
        >>> d.add(1)
        >>> d.add(2)
        >>> d.add_to_front(3)
        >>> print(d)
        [3, 1, 2]
        """
        
        self._content.insert(0,obj)
        
    def remove_from_end(self):
        """
        Remove and return the last object from Queue self
        Deque self must not be empty.
        Extends class Queue. This is a new method.
        :rtype: object
        >>> d = Deque()
        >>> d.add(1)
        >>> d.add(2)
        >>> d.remove_from_end()
        2
        """        
        self._content.pop()
        
class Pqueue_prepare_time(Queue):
    """
    A priority queue, called Pqueue
    """
    def __init__(self):
        """
        Create and initialize new Pqueue self.
        
        Precondition: a_priority must be one of the attributes that all
        elements that will be added to Pqueue self have
        
        :param a_priority: one of the attributes of the elements that will
        be added to the Pqueue self
        :type a_priority: str
        """
        super(Pqueue_prepare_time, self).__init__()
        
    def remove(self):
        """
        Remove and return the element from Pqueue self, based on priority
        Pqueue self must not be empty.
       
         Overrides Deque.remove()
        :rtype: object

        >>> pq = Pqueue("profit")
        >>> pq.add(Person("Sara",65))
        >>> pq.add(Person("Mike",60))
        >>> pq.add(Person("Jessica",75))
        >>> print(pq.remove())
        Mike 60
        >>> print(pq.remove())
        Sara 65
        >>> print(pq.remove())
        Jessica 75
        """
        
        index = 0
        # see the note below for further information on __getattribute__
        priority = self._content[0].prepare_time()
        i = 1
        while i < len(self._content):
    #having an issue with 
            if self._content[i].prepare_time() < priority:
                priority = self._content[i].prepare_time()
                index = i
            i+=1
        return self._content.pop(index)

class Pqueue_profit(Queue):
    """
    A priority queue, called Pqueue
    """
    def __init__(self):
        """
        Create and initialize new Pqueue self.
        
        Precondition: a_priority must be one of the attributes that all
        elements that will be added to Pqueue self have
        
        :param a_priority: one of the attributes of the elements that will
        be added to the Pqueue self
        :type a_priority: str
        """
        super(Pqueue_profit, self).__init__()
        
    def remove(self):
        """
        Remove and return the element from Pqueue self, based on priority
        Pqueue self must not be empty.
       
         Overrides Deque.remove()
        :rtype: object

        >>> pq = Pqueue("profit")
        >>> pq.add(Person("Sara",65))
        >>> pq.add(Person("Mike",60))
        >>> pq.add(Person("Jessica",75))
        >>> print(pq.remove())
        Mike 60
        >>> print(pq.remove())
        Sara 65
        >>> print(pq.remove())
        Jessica 75
        """
        
        index = 0
        # see the note below for further information on __getattribute__
        priority = self._content[0].profit()
        i = 1
        while i < len(self._content):
    #having an issue with 
            if self._content[i].profit() < priority:
                priority = self._content[i].profit()
                index = i
            i+=1
        return self._content.pop(index)
