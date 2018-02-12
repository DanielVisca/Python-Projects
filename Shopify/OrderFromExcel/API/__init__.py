from API.Queue import Queue
from API.ReadExcel import ReadExcel
from API.ReadQueue import ReadQueue
from API.Store import Store
"""
This Program reads from an Excel file, adds each line of the file to a queue (For Scalability). The class 'ReadQueue',
reads each item in the Queue, accesses the store as an admin and places an order for the Product.
"""

if __name__ == "__main__":
    # Create known store 'jelly' and fill in the info to access the API
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

