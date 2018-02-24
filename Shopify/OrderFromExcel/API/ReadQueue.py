import requests
from API.Order import Order
import base64
from os.path import normpath, basename


class ReadQueue:
    """
    Reads items from Queue, if the item is a shop an admin connection is made with it given that it is a known shop,
    if it is an email an order is created that customer, if it is a product it gets added to the order.
    """

    def __init__(self, queue, known_stores):
        """
        Initialize Reading from the Queue, connecting to known stores and ordering products for the given customer.

        :param self:
        :param queue: Queue
        :param known_stores: list of stores
        """
        self.order_queue = queue
        self.email = ""
        self.shop_name = ""
        self.new_order = None
        self.known_stores = known_stores
        self.accept_orders = False
        self.query_from_queue()

    # make orders
    def read_queue(self):
        while not self.order_queue.is_empty():
            order = self.order_queue.remove()

    # Called when class is initialized
    def query_from_queue(self):
        while not self.order_queue.is_empty:
            order = self.order_queue.remove()
            self.new_order = Order(order["shop"], order["email"])
            # Now I need to add the items and quantity to the order. To do this, I need the variant_ids
            #product_titles = []
            #for product in self.new_order["products"]:

    # def query_from_queue(self):
        # """
        # For every item in the queue, make the given query
        #
        # :param self:
        # :return: NoneType
        # """
        # while not self.order_queue.is_empty():
        #     line = self.order_queue.remove()
        #
        #     if line[0] == "email":
        #         self.is_email(line)
        #
        #     elif line[0] == "shop":
        #         self.is_shop(line)
        #
        #     else:
        #         # Only accepts orders when the shop is a known shop
        #         if not self.accept_orders or line[0] == "":
        #             continue
        #
        #         self.is_product(line)

    # Helper Function for query_from_queue
    def is_email(self,line):
        """
        Set the email of the customer and close any previous orders.

        :param line: list of strings
        :return: NoneType
        """
        if self.email != "":
            self.new_order.complete()
            self.new_order = Order(self.store, line[1])
        self.email = line[1]

    # Helper Function for query_from_queue
    def is_shop(self, line):
        """
        Set the Shop and check if it is a known store

        :param line: list of strings
        :return: NoneType
        """
        shop_name = line[1].replace(" ", "").lower()

        # Check known stores for store
        known_store = None
        for store in self.known_stores:
            if store.name == shop_name:
                self.store = store
                known_store = store
                self.accept_orders = True
                break

        if self.new_order is not None and known_store is not None:
            self.new_order.complete()

        if known_store is None:
            self.new_order.complete()
            self.accept_orders = False
            print(shop_name + " is not a known Store")
            # This will cause an error when a product is ordered

        # For some reason if I put an unknoen store at the end. The store above it does not order.
        self.new_order = Order(self.store, self.email)

    # Helper Function for query_from_queue
    def is_product(self, line):
        """
        Add the product to the Order and complete the Order if it is the last item

        :param line: list of strings
        :return: NoneType
        """
        self.product = self.prod_to_id(line[0])
        self.quantity = int(line[1])
        item = {"variant_id": self.product, "quantity": int(self.quantity)}
        self.new_order.add_item(item)
        if self.order_queue.is_empty():
            self.new_order.complete()

    # Helper Function for is_product
    def prod_to_id(self, products):
        """
        Precondition: the product name must be similar to the product handle as made by the store owner:
            Ex: product "Almond Butter", handle "almond-butter". This will work
                product "Almond Butter", handle "coffee". This will not work

        Return the variant id given a product title

        :param self:
        :param product: List of String
        :return: String
        """
        # ToDo make one query for all products
        #query = '{shop{products(first:1, query:"title='
        #for product in products:
            #query += '{shop{products(first:1, query:"title=' \
            #'' + product + '"){edges{node{variants(first:1){edges{node{id}}}}}}}}'
        product = products.replace(" ","-").lower()
        # graphQL query
        query = '{shop{products(first:1, query:"title=' \
                '' + product + '"){edges{node{variants(first:1){edges{node{id}}}}}}}}'

        response = self.make_query(query)
        # variant_id is returned as a scalar
        encoded_variant_id = response['data']['shop']['products']['edges'][0]['node']['variants']['edges'][0]['node']['id']
        decoded_variant_id_url = base64.b64decode(encoded_variant_id)
        # convert tp string
        decoded_variant_id = basename(normpath(decoded_variant_id_url)).decode("utf-8")
        return decoded_variant_id

    def make_query(self, query):
        """
        Precondition: Query must be in graphQL format

        Return query response

        :param query: String
        :return: Dict
        """

        request = requests.post(self.store.get_url_graphQL(), json={'query': query}, headers=self.store.get_headers())
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

if __name__ == '__main__':
    pass