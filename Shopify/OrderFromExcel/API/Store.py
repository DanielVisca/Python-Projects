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
        Set the Stores Header value (Key is already known). This allows for Queries to be made to the store

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

if __name__ == "__main__":
    pass
