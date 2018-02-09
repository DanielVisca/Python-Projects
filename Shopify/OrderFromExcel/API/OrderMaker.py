import requests
from API.Order import Order

"""
Personal note:  - because I take in and save the queue, the original queue may remain unchanged. This would not be scalable. Make sure thisis not the case
                - if one line returns an error, skip to the next
"""
class Store:
    """
    Connect to the graphQL endpoint of given Shopify stores, Headers are necessary

    Before making a query the appropriate headers as well as shop name must be added
    """
    def __init__(self,queue):
        """
        Initialize graphQL
        """
        self.order_queue = queue
        self.email = ""
        self.shop_name = ""
        self.new_order = None


    def make_query(self, query):
        """
        Return query response

        :param query: String
        :return: Dict
        """
        request = requests.post(self.url, json={'query': query}, headers=self.headers)
        if request.status_code == 200:
            print(request.json())
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


    def query_from_queue(self):
        """
        For every item in the queue, make the given query

        :param query:
        :return:
        """

        #currently the line does nothing.  need to decide on what to do here
        while not self.order_queue.is_empty():
            line = self.order_queue.remove()
            if line[0] == "email":
                self.email = line[1]

            elif line[0] == "shop":
                self.shop_name = line[1]

                if self.new_order != None:
                    self.new_order.complete()

                self.new_order = Order(self.email)

            #could be referenced before existing
            else:
                self.product = int(line[0])
                self.quantity = int(line [1])
                item = {"variant_id": int(self.product), "quantity": int(self.quantity)}
                self.new_order.add_item(item)
                if self.order_queue.is_empty():
                    self.new_order.complete()
