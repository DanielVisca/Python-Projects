from API.Queue import Queue
from API.ReadExcel import ReadExcel
from API.OrderMaker import ReadQueue
from API.Store import Store

# known stores
jelly = Store("Jubilant Jelly")
jelly.set_api_key("304f648523a9a6addecf48d0002c24e1")
jelly.set_password("0312f477ae629b38a2c6dc2fdf71e7b2")
jelly.update_url_with_password()
jelly.update_url()
jelly.set_headers("X-Shopify-Storefront-Access-Token", "8e720fe93c5e9455d1a8a0191c1e0a37")

jam = Store("Jubilant Jam")
jam.set_api_key("bd6f9a751545db3d577d78cb2b63223b")
jam.set_password("1bf61789bbb3ba88ae5b8bee6bc220ed")
jam.update_url_with_password()
jam.update_url()
jam.set_headers("X-Shopify-Storefront-Access-Token", "462e6557ff3cf5dbda92eccb56ee85ea")

known_stores = [jelly, jam]

q = Queue()
r = ReadExcel("OrderFromThisExcelFile", q)
r.order_from_excel()
rq = ReadQueue(q, known_stores)
rq.query_from_queue()

# rq.add_headers("X-Shopify-Storefront-Access-Token", "8e720fe93c5e9455d1a8a0191c1e0a37" )
# rq.add_store_name("Jubilant Jelly")
# rq.make_query("{shop{name}}")
# rq.api_call("products")
# rq.prod_to_id("coffee")
