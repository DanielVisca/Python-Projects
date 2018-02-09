from API.Queue import Queue
from API.ReadExcel import ExcelOrder
from API.OrderMaker import Store

q = Queue()
r = ExcelOrder("OrderFromThisExcelFile",q)
r.order_from_excel()
om = Store(q)
om.query_from_queue()