class Queue:
    """
    FIFO (first in first out)
    """

    def __init__(self):
        """
        Create and initialize a new queue self.

        :return: NoneType
        """
        self._data = []

    def add(self, prod):
        """
        Add prod at the back of this queue.

        :param prod:
        :return: NoneType
        """
        self._data.append(prod)

    def remove(self):
        """
        Remove and return front object from self.

        :return: Object

        >>> q = Queue()
        >>> q.add("bath bombs")
        >>> q.add("babel fish")
        >>> q.remove()
        "bath bombs"
        """
        return self._data.pop(0)

    def is_empty(self):
        """
        Return True when queue self is empty, False otherwise.

        :return: bool

        >>> q = Queue()
        >>> q .add("Ray Banz")
        >>> q.is_empty()
        False
        >>> q.remove()
        "Ray Banz"
        >>> q.is_empty()
        True
        """
        return self._data == []


import requests
import base64
from os.path import normpath, basename

# from API.Store import Store
# import json

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
        self.accept_orders = False

    def query_from_queue(self):
        """
        For every item in the queue, make the given query

        :param self:
        :return: NoneType
        """
        while not self.order_queue.is_empty():
            line = self.order_queue.remove()

            if line[0] == "email":
                self.is_email(line)

            elif line[0] == "shop":
                self.is_shop(line)

            else:
                # Only accepts orders when the shop is a known shop
                if not self.accept_orders or line[0] == "":
                    continue

                self.is_product(line)

    # Helper Function for query_from_queue
    def is_email(self, line):
        """
        Set the email of the customer and close any precious orders

        :param line: list of strings
        :return: NoneType
        """
        if self.email != "":
            self.new_order.complete()
            self.new_order = Order(self.store, line[0])
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
        :return:
        """
        self.product = self.prod_to_id(line[0])
        self.quantity = int(line[1])
        item = {"variant_id": self.product, "quantity": int(self.quantity)}
        self.new_order.add_item(item)
        if self.order_queue.is_empty():
            self.new_order.complete()

    # Helper Function for is_product
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
        product = product.replace(" ", "-").lower()
        # graphQL query
        query = '{shop{products(first:1, query:"title=' \
                '' + product + '"){edges{node{variants(first:1){edges{node{id}}}}}}}}'

        response = self.make_query(query)
        # variant_id is returned as a scalar
        encoded_variant_id = response['data']['shop']['products']['edges'][0]['node']['variants']['edges'][0]['node'][
            'id']
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


import xlrd
import os


class ReadExcel:
    """
    Take in an Excel sheet, for every line create an order request.
    Every order request will be added to a Queue.

    Precondition: Excel File format: The email of the client must be in the first row. And the shop to order from must
    be in the second row. All following products will be ordered from the given shop until a new shop is specified.
    Confirmation will be sent to the given email until a new email is specified:
        Ex format:
        email               |  client@email.com
        shop                |  Jubilant Jelly
        Almond Butter       |  4
        Jelly Fish Sandwich |  2
        shop                |  Jubilant Jam
        Peanut Butter       |  1
    """

    def __init__(self, excelFile, queue):
        """
        initialize Excel order
        :param excelFile: The name and file type of the excel file to be ordered from
        """
        # Personal Note: Should I have the queue existing in each instance or elsewhere?
        # Answer: I should have it exist elsewhere, that way if several excel sheets are being ordered from at the same time their wont be any overlap
        self.excelFile = excelFile
        self.order_queue = queue

    def order_from_excel(self):
        """
        Assume file ends in '.xlsx'
        Make a an order request for every product in the excel file

        :return: NoneType
        """

        file_location = os.path.dirname(os.path.abspath(__file__)) + "/" + self.excelFile + ".xlsx"

        # file_location = "C:/Users/danie/desktop/" + self.excelFile + ".xlsx"
        workbook = xlrd.open_workbook(file_location)

        for i in range(workbook.nsheets):
            sheet = workbook.sheet_by_index(i)
            for n in range(sheet.nrows):
                line = [sheet.cell_value(n, 0), sheet.cell_value(n, 1)]
                self.request(line)

    def request(self, product):
        """
        Make a buy request for the given product and add to Queue
        :param product: the product to be purchased
        :return: NoneType
        """
        self.order_queue.add(product)

import shopify


class Order():
    def __init__(self, store, email):
        """
        Initialize an order

        :param self:
        :param store: Store  This is the store that the order will be created for
        :param email: The email of the client
        """
        self.store_name = store.get_name()

        shopify.ShopifyResource.set_site(store.get_password_url())
        self.shop = shopify.Shop.current()

        #create new order
        self.order = shopify.Order()
        self.order.email = email
        self.order.send_fulfillment_receipt = False

        #Mark the order status as fulfilled. ToDo: Actually fulfill the order instead of just marking it as such
        self.order.fulfillment_status = "fulfilled"
        self.order.send_receipt = True
        self.order.line_items = []

    def add_item(self, item):
        """
        Add an item to the order

        :param item: dict eg: {"variant_id": 1234567, "quantity": 4 }
        :return: Nonetype
        """
        self.order.line_items.append(item)

    def complete(self):
        """
        Complete the Order

        :return: NoneType
        """
        success = self.order.save()
        if success:
            print("Order was successful at " + self.store_name )
        else:
            print("order was unsuccessful at " + self.store_name )


class Store:
    """
    Create a Store with information of how to contact it through API.
    On creation the store has attributes 'url' and 'name'.
    When fully updated it has attributes 'url', 'name', 'api_key', 'password', 'password_url', 'headers'.
    """
    def __init__(self, name):
        """
        Initialize a Store
        :param name: String
        """
        self.name = name.replace(" ", "").lower()
        self.update_url()

    def get_name(self):
        return self.name

    def set_api_key(self, api_key):
        """
        Set the stores API key

        :param api_key:
        :return:
        """
        self.api_key = api_key

        # When both api_key and password exist for the store, update the url to access admin
        if hasattr(self, 'password'):
            self.update_url_with_password()

    def get_api_key(self):
        return self.api_key

    def set_password(self, password):
        self.password = password

        # When both api_key and password exist for the store, update the url to access admin
        if hasattr(self, 'api_key'):
            self.update_url_with_password()

    def get_password(self):
        return self.password

    # Helper Function
    def update_url_with_password(self):
        """
        When the api_key and password have been added, create the URL to access admin info

        :return: NoneType
        """
        self.password_url = "https://%s:%s@%s.myshopify.com/admin" % (self.api_key, self.password, self.name)

    def get_password_url(self):
        return self.password_url

    def set_header_value(self, value):
        """
        Set the Stores Header value (Key is already known)

        :param value: String
        :return:
        """
        key = "X-Shopify-Storefront-Access-Token"
        self.headers = {key: value}

    def get_headers(self):
        return self.headers

    # Helper Function
    def update_url(self):
        self.url_graphQL = 'https://' + self.name + '.myshopify.com/api/graphql'
        self.url = 'https://' + self.name + '.myshopify.com/admin'

    def get_url_graphQL(self):
        return self.url_graphQL

    def get_url(self):
        return  self.url

    def get_url(self):
        return self.url

    def get_url_graphQL(self):
        return self.url_graphQL


jelly = Store("Jubilant Jelly")
jelly.set_api_key("304f648523a9a6addecf48d0002c24e1")
jelly.set_password("0312f477ae629b38a2c6dc2fdf71e7b2")
jelly.set_header_value("8e720fe93c5e9455d1a8a0191c1e0a37")

# Create known store 'jam' and fill in the info to access the API
jam = Store("Jubilant Jam")
jam.set_api_key("bd6f9a751545db3d577d78cb2b63223b")
jam.set_password("1bf61789bbb3ba88ae5b8bee6bc220ed")
jam.set_header_value("462e6557ff3cf5dbda92eccb56ee85ea")

# all known stores that this program will be abe to access
known_stores = [jelly, jam]

q = Queue()
r = ReadExcel("OrderFromThisExcelFile", q)
r.order_from_excel()
rq = ReadQueue(q, known_stores)
rq.query_from_queue()