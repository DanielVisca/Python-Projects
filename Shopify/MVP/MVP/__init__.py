from MVP.graphQL import GraphQL
from MVP.Queue import Queue
from MVP.OrderFromExcelSheet import Excel_order
"""
Personal note: "from x.y import z" is sloppy. use "if __name__ == "__main__":" correctly and fix this
"""
if __name__ == "__main__":

    #create Queue that will hold all requests
    q = Queue()

    e = Excel_order("ShopifyProducts", q)
    #Add all requests to Queue
    e.order_from_excel()

    g = GraphQL(q)

    #make query for every item on Queue
    g.query_from_queue()
