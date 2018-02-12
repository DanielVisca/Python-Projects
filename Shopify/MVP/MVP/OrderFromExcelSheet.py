import xlrd
import os

class Excel_order:
    """
    Take in an Excel sheet, for every line create an order request.
    Every order request will be added to a Queue.

    extra additions to keep in mind:
    -give an approx. wait time
    """

    def __init__(self, excelFile, queue):
        """
        initialize Excel order
        :param excelFile: The name and file type of the excel file to be ordered from
        """
        #Personal Note: Should I have the queue existing in each instance or elsewhere?
        #Answer: I should have it exist elsewhere, that way if several excel sheets are being ordered from at the same time their wont be any overlap
        self.excelFile = excelFile
        self.order_queue = queue

    def order_from_excel(self):
        """
        Assume file ends in '.xlsx'
        Make a an order request for every product in the excel file

        :return: NoneType
        """

        file_location =  os.path.dirname(os.path.abspath(__file__)) +"/" +  self.excelFile + ".xlsx"

        #file_location = "C:/Users/danie/desktop/" + self.excelFile + ".xlsx"
        workbook = xlrd.open_workbook(file_location)

        for i in range(workbook.nsheets):
            sheet = workbook.sheet_by_index(i)
            for n in range(sheet.nrows):
                line = [sheet.cell_value(n, 0),sheet.cell_value(n, 1)]
                self.request(line)

    def request(self, product):
        """
        Make a buy request for the given product and add to Queue
        :param product: the product to be purchased
        :return: NoneType
        """
        self.order_queue.add(product)

