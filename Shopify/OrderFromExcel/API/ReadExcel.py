import xlrd
import os


class ReadExcel:
    """
    Take in an Excel sheet, for every line create an order request.
    Every order request will be added to a Queue.

    Precondition: Excel File format: The email of the client must be in the first row. And the shop to order from must
    be in the second row. All following products will be ordered from the given shop until a new shop is specified.
    Confirmation will be sent to the given email until a new email is specified:
        Ex format:
        email               |  client@email.com
        shop                |  Jubilant Jelly
        Almond Butter       |  4
        Jelly Fish Sandwich |  2
        shop                |  Jubilant Jam
        Peanut Butter       |  1
    """

    def __init__(self, excelFile, queue):
        """
        initialize Excel order
        :param excelFile: The name and file type of the excel file to be ordered from
        """
        self.email = ""
        self.excelFile = excelFile
        self.order_queue = queue
        self.order_info = {"email": self.email}
        self.end = False

    def accumulate_order(self, line):
        """
        Accumulate all of the info required for an Order

        Personal Note: Info required for an order from the Excel File. An Email, a Shop, all products unitil next order
                        or end of file.

        :param line: list of Strings
        :return: NoneType
        """
        if line[0] == "email":
            self.email = line[1]
            self.order_info["email"] = line[1]

        elif line[0] == "shop":
            if self.valid_order():
                # send order request
                self.request(self.order_info)
            #
            # if "email" not in self.order_info:
            #     self.order_info["email"] = self.email

            # create new order info with new shop
            self.order_info = {"shop": line[1], "email": self.email}

        # Assumes everything else is a product, this should be double checked when the API is contacted
        else:
            # Check if empty line
            if line[0] != "":
                # Set default quantity if none is provided
                if line[1] == "":
                    line[1] = "1"

                if "products" in self.order_info:
                    self.order_info["products"].append((line[0], int(line[1])))
                else:
                    # if no quantity it set, set it to 1
                    if line[1] == "":
                        line[1] = "1"
                    self.order_info["products"] = [(line[0], int(line[1]))]
            if self.end and self.valid_order():
                self.request(self.order_info)

        # must check if next line is empty

    def order_from_excel(self):
        """
        Assume file ends in '.xlsx'
        Make a an order request for every product in the excel file

        :return: NoneType
        """

        file_location = os.path.dirname(os.path.abspath(__file__)) + "/" + self.excelFile + ".xlsx"

        # file_location = "C:/Users/danie/desktop/" + self.excelFile + ".xlsx"
        workbook = xlrd.open_workbook(file_location)

        for i in range(workbook.nsheets):
            sheet = workbook.sheet_by_index(i)
            for n in range(sheet.nrows):
                line = [sheet.cell_value(n, 0), sheet.cell_value(n, 1)]
                # I don't believe this will work with multiple sheets
                if n + 1 == sheet.nrows:
                    self.end = True
                self.accumulate_order(line)

    def request(self, product):
        """
        Make a buy request for the given product and add to Queue
        :param product: the product to be purchased
        :return: NoneType
        """
        self.order_queue.add(self.order_info)

    def valid_order(self):
        """
        Return if self has enough information to make a valid order

        :return: Bool
        """

        if (self.order_info["email"] != "") and ("products" in self.order_info) and ("shop" in self.order_info):
            return True
        else:
            return False



if __name__ == '__main__':
    pass
