import requests
from API.Order import Order
from API.Store import Store
import json

"""
Personal note:  - because I take in and save the queue, the original queue may remain unchanged. This would not be scalable. Make sure thisis not the case
                - if one line returns an error, skip to the next
"""


class ReadQueue:
    """
    Connect to the graphQL endpoint of given Shopify stores, Headers are necessary

    Before making a query the appropriate headers as well as shop name must be added
    """

    def __init__(self, queue, known_stores):
        """
        Initialize graphQL
        """
        self.order_queue = queue
        self.email = ""
        self.shop_name = ""
        self.new_order = None
        self.known_stores = known_stores

    def query_from_queue(self):
        """
        Personal Note: #This is messy. Breakdown of what I want to do. pop from queue,
        freely add products to the cart, (if an order is attempted to be completed before it can, throw an error).
        An order cannot be completed unless the shop name is provided and an email is provided. if the first row
         says email, add the email, if it says shop add the shop.
        Broken down the rules are... always add a product to the cart(this has to be an else function. When the queue
         is empty, order. When an email is added and their previously existed an email, order the cart then update the email.
        When a new shop is listed, the cart does not necessarily need to be ordered right away because maybe more
        products will be added after (side effect of being able to add products without specifying a store(problem cant
        do that. cant add an item to the cart if I dont know the store. Precondition Shop must be specified before
        products. email isnt necessary until the end.
        pop from queue
        freely add products to the cart
        order cannot be completed unless the shop name is provided and an email is provided.
        if the first row
        says email, add the email, if it says shop add the shop.
        When the queue is empty, order

        For every item in the queue, make the given query

        :param query:
        :return:
        """

        while not self.order_queue.is_empty():
            line = self.order_queue.remove()
            if line[0] == "email":
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

                self.new_order = Order(store, self.email)

            # could be referenced before existing
            else:
                self.product = self.prod_to_id(line[0])
                self.quantity = int(line[1])
                item = {"variant_id": self.product, "quantity": int(self.quantity)}
                self.new_order.add_item(item)
                if self.order_queue.is_empty():
                    self.new_order.complete()

    def prod_to_id(self, product):
        """
        return the variant id of the given product
        :param self:
        :param product:
        :return:
        """
        dict = {"Almond Butter": "6797069778989", "Peanut Butter": "1573432655890",
                "Jelly Fish Sandwich": "6862783905837"}
        if dict[product]:
            return dict[product]
        # currently using REST, I want to us graphQL
        # the url could potentially have '/admin' in it already
        #
        # products = self.api_call("/products.json")
        # print(products)
        # variant_id = ""
        # for item in products:
        #     print(item)
        #     if item["title"] == self.product:
        #         variant_id = item["variants"]["id"]
        # if variant_id == "":
        #     return "An Item you asked for does not exist with that name"
        #         # Manual Query
        # else:
        #     return variant_id
    # def add_headers(self, key, value):
    #     """
    #     Add a header to self
    #
    #     :param key: String
    #     :param value: String
    #     :return: NoneType
    #     """
    #     self.headers = {key: value}


    # def add_store_name(self, store_name):
    #     """
    #     Pesonal Note: Make it clear that this should be the same as the storename seen in the url
    #     Add store name to self, convert to
    #     currently doesnt convert to useful format for some reason
    #     :param store_name: String
    #     :return:
    #     """
    #     # Convert to useful format
    #     self.store_name = store_name.replace(" ", "")
    #     self.store_name = self.store_name.lower()
    #     self.url = 'https://' + self. store_name + '.myshopify.com'

    def make_query(self, query, graphQL=True):
        """
        Return query response

        :param query: String
        :return: Dict
        """
        # self.url = self.new_order.shop_url
        # self.add_headers(self.new_order.API_KEY, self.new_order.PASSWORD)
        if graphQL:
            url = self.store.get_url_graphQL()
        else:
            url = self.store.get_url
        request = requests.post(url, json={'query': query}, headers=self.store.get_headers())
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    def api_call(self, query):
        return None
        # url = self.store.get_url() + query
        # response = requests.get()
        # if response.status_code == 200:
        #     print(json.loads(response.content.decode('utf-8')))
        #     return json.loads(response.content.decode('utf-8'))
        # else:
        #     return []


        # request = requests.post("https://jubilantjelly.myshopify.com/admin/products.json", headers=self.store.get_headers())
        # if request.status_code == 200:
        #     return request.json()
        # else:
        #     raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        #temp:

