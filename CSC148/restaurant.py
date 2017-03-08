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
        #TODO: Complete this part


    def add_customer(self, new_customer):
        """Add a new entering customer to the restaurant.

        :type new_customer: Customer
            The new customer that is entering the restaurant
        :rtype: None
        """
        #TODO: Complete this part

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
        
        >>> t = MaxApproach()
        >>> t.add_customer(Customer("1 345336 6 7 8"))
        >>> t.process_turn(1)
        >>> print(len(t.line_up))
        0
        """
        #TODO: Complete this part


    def write_report(self, report_file):
        """Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None
        """
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
