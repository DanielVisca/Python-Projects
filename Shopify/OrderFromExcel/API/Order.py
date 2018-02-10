import shopify


class Order():
    def __init__(self, store, email):
        """
        Initialize an order

        """
        # self.API_KEY = '304f648523a9a6addecf48d0002c24e1'
        # self.PASSWORD = '0312f477ae629b38a2c6dc2fdf71e7b2'
        # self.SHOP_NAME = 'jubilantjelly'
        print(store.get_password)
        #   self.shop_url = store.password_url #"https://%s:%s@%s.myshopify.com/admin" % (store.get_api_key(), store.get_password(), store.get_name())
        shopify.ShopifyResource.set_site(store.get_password_url())
        self.shop = shopify.Shop.current()

        self.order = shopify.Order()
        self.order.email = email
        # self.order.note = "A very important note"
        # eventually this should be properly fulfilled an not manually entered
        self.order.fulfillment_status = "fulfilled"
        self.order.send_receipt = True
        self.order.send_fulfillment_receipt = False
        self.order.line_items = []

    def add_item(self, item):
        """
        Add an item to the order

        :param item: dict eg: {"variant_id": 1234567, "quatity": 4 }
        :return: Nonetype
        """
        # Place tests here to see if this is proper format
        self.order.line_items.append(item)

    def complete(self):
        """
        Personal Note: Throw an Error if incomplete
        Complete the Order

        :return: NoneType
        """
        success = self.order.save()
        print(success)

    def update_key_and_password(self, API_KEY, PASSWORD):
        """
        Update the API key

        :param API_KEY: Integer
        :return: NoneType
        """
        self.API_KEY = API_KEY
        self.PASSWORD = PASSWORD

    def update_shop_name(self, shop_name):
        """
        Update the Shops name

        :param shop_name:
        :return:
        """
        self.SHOP_NAME = shop_name

    def update_url(self):
        """
        Update the url after Shop_name, key_and_password are updated

        :return: NoneType
        """
        self.shop_url = "https://%s:%s@%s.myshopify.com/admin" % (self.API_KEY, self.PASSWORD, self.SHOP_NAME)
