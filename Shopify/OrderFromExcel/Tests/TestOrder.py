from API import Order, Store
import unittest

class TestOrder(unittest.TestCase):

    def __init__(self):
        """
        Design Notes: I dont like that a store has to be created here,
               And if my store goes offline or the test product is removed
               my test will fail.
        """
        self.store = Store("Jubilant Jelly")
        self.store.set_api_key("304f648523a9a6addecf48d0002c24e1")
        self.store.set_password("0312f477ae629b38a2c6dc2fdf71e7b2")
        self.store.set_header_value("8e720fe93c5e9455d1a8a0191c1e0a37")

    def test_add_item(self):

        self.order = Order(self.store, "danielvisca96@gmail.com")

        # Confirm nothing will be ordered
        self.assertEqual(self.order.line_items,  [])

        # Add Peanut Butter to order
        self.order.add_item("1573432655890")
        self.assertEqual(self.order.line_items, ["1573432655890"])

    def test_complete(self):
        """
        Testing order would be testing Shopifys package, this is redundant
        :return:
        """
        # if self.hasattr("order"):
        #    self.order.complete()

if __name__ == "__main__":
    # Not currently functioning, this is where I am at now
    unittest.main()

