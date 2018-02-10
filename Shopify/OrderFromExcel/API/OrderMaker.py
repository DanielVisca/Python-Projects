import requests
from API.Order import Order
import base64
from os.path import normpath, basename

#from API.Store import Store
#import json

"""
Personal note:  - because I take in and save the queue, the original queue may remain unchanged. This would not be
                scalable. Make sure this is not the case
                - if one line returns an error, skip to the next
                -Somehow two instances of this are made at the same time, This creates a double order! Also possibly the
                cause of the self error
"""


class ReadQueue:
    """
    Connect to the graphQL endpoint of given Shopify stores, Headers are necessary

    Before making a query the appropriate headers as well as shop name must be added
    """

    def __init__(self, queue, known_stores):
        """
        Initialize Reading from the Queue

        :param self:
        :param queue: Queue
        :param known_stores: list of stores
        """
        self.order_queue = queue
        self.email = ""
        self.shop_name = ""
        self.new_order = None
        self.known_stores = known_stores

    def query_from_queue(self):
        """
        For every item in the queue, make the given query

        :param self:
        :return: NoneType
        """
        while not self.order_queue.is_empty():
            line = self.order_queue.remove()
            if line[0] == "email":
                if self.email != "":
                    self.new_order.complete()
                    self.new_order = Order(store,line[0])
                self.email = line[1]

            elif line[0] == "shop":
                shop_name = line[1].replace(" ", "").lower()

                # Check known stores for store
                for store in self.known_stores:
                    if store.name == shop_name:
                        self.store = store
                        break
                # Throw an error if the store is not known!!

                if self.new_order != None:
                    self.new_order.complete()

                self.new_order = Order(self.store, self.email)

            # This does not account for blank lines, typos etc...
            else:
                self.product = self.prod_to_id(line[0])
                self.quantity = int(line[1])
                item = {"variant_id": self.product, "quantity": int(self.quantity)}
                self.new_order.add_item(item)
                if self.order_queue.is_empty():
                    self.new_order.complete()

    def prod_to_id(self, product):
        """
        Precondition: the product name must be similar to the product handle as made by the store owner:
            Ex: product "Almond Butter", handle "almond-butter". This will work
                product "Almond Butter", handle "coffee". This will not work

        Return the variant id of the given product

        :param self:
        :param product: String
        :return: String
        """
        product = product.replace(" ","-").lower()
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

        # dict = {"Almond Butter": "6797069778989", "Peanut Butter": "1573432655890",
              #  "Jelly Fish Sandwich": "6862783905837"}

    def make_query(self, query):
        """
        Return query response

        :param query: String
        :param graphQL: Boolean  clarify if the query is for a graphQL API
        :return: Dict
        """

        request = requests.post(self.store.get_url_graphQL(), json={'query': query}, headers=self.store.get_headers())
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

if __name__ == '__main__':
    pass