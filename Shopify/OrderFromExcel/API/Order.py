import shopify


class Order:

    def __init__(self, store, email):
        """
        Preconditions: Store must have an api_key and password attribute.

        Initialize an order with no items, mark as payment fulfilled.

        :param self:
        :param store: Store  This is the store that the order will be created for
        :param email: The email of the client
        """

        self.store_name = store.get_name()

        shopify.ShopifyResource.set_site(store.get_password_url())
        self.shop = shopify.Shop.current()

        # create new order
        self.order = shopify.Order()
        self.order.email = email
        self.order.send_fulfillment_receipt = False

        # Mark the order status as fulfilled. ToDo: Actually fulfill the order instead of just marking it as such
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
        Complete the Order, receipt will be sent to the customers email.

        :return: NoneType
        """
        success = self.order.save()
        if success:
            print("Order was successful at " + self.store_name )
        else:
            print("order was unsuccessful at " + self.store_name )

if __name__ == '__main__':
    pass