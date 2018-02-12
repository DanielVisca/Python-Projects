import requests
"""
Personal note:  - because I take in and save the queue, the original queue may remain unchanged. This would not be scalable. Make sure thisis not the case
                - if one line returns an error, skip to the next
"""
class GraphQL:
    """
    Connect to the graphQL endpoint of given Shopify stores, Headers are necessary
    """
    def __init__(self,queue):
        """
        Initialize graphQL
        """
        self.order_queue = queue


    def make_query(self, query, headers):
        """
        Return query response

        :param query: String
        :return: Dict
        """
        request = requests.post(self.url, json={'query': query}, headers=headers)
        if request.status_code == 200:
            print(request.json())
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    def add_headers(self, key, value):
        """
        Add a header to self

        :param key: String
        :param value: String
        :return: NoneType
        """
        self.headers = {key : value}

    def add_store_name(self, store_name):
        """
        Pesonal Note: Make it cleare that this should be the same as the storename seen in the url
        Add store name to self, convert to url

        :param store_name: String
        :return:
        """
        #Convert to useful format
        store_name.replace(" ", "")
        store_name.lower()
        self.url = 'https://' + store_name + '.myshopify.com/api/graphql'

    def direct_query(self,store_url, headers, query):
        """
        make a query with only the information provided

        :param store_url:
        :param header:
        :param query:
        :return:
        """

        request = requests.post(store_url + '/api/graphql', json={'query': query}, headers=headers)
        if request.status_code == 200:
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
            self.add_store_name(line[0])
            self.add_headers("X-Shopify-Storefront-Access-Token",line[1])
            print(self.headers)
            self.make_query("{shop {name}}",self.headers)
