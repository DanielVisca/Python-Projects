class Store:
    def __init__(self, name):
        self.name = name.replace(" ", "").lower()

    def set_api_key(self, API_KEY):
        self.api_key = API_KEY

    def set_password(self, password):
        self.password = password

    def update_url_with_password(self):
        self.password_url = "https://%s:%s@%s.myshopify.com/admin" % (self.api_key, self.password, self.name)

    def set_headers(self, key, value):
        self.headers = {key: value}

    def update_url(self):
        self.url_graphQL = 'https://' + self.name + '.myshopify.com/api/graphql'
        self.url = 'https://' + self.name + '.myshopify.com/admin'

    def get_name(self):
        return self.name

    def get_api_key(self):
        return self.api_key

    def get_password(self):
        print(self.password)
        return self.password

    def get_password_url(self):
        return self.password_url

    def get_url(self):
        return self.url

    def get_headers(self):
        return self.headers

    def get_url_graphQL(self):
        return self.url_graphQL
