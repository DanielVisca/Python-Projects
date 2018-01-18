import json
import requests
"""
GET https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/data.{return_format}

Can get Revenue from:
https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.csv?ticker=AAPL&qopts.columns=ticker,dimension,datekey,revenue&api_key=2mDaZDV4cJgNjkzvf24u"
The above call returns the net quarterly sales revenue for AAPL, in CSV format.

Can get stock prices from
"https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=2mDaZDV4cJgNjkzvf24u"
The above call gets all AAPL stock prices, sorted in descending date order, in JSON format.

Market Value (as priced by outstanding shares(total number of owned shares)

Use the "times revenue method" multiply the years revenue that should be the maximum valuation  of that given company
"""
class StockValue:

    def __init__(self, ticker):
        self.ticker = ticker

        self.API = self.getAPI()
        self.RevAPI = self.getRevAPI()

        self.revenue = self.getRev()
        self.stockPrice = self.getDayPrice()
        #number that changed hands during a given day
        self.volume = self.getVolume()
        print(self.volume)
        print (self.stockPrice)
        self.calculatedValuation = int(self.volume) * int(self.stockPrice)
        print(self.calculatedValuation)

    def getAPI(self,):
        """
        Ticker must be in CAPS
        ticker must be in NASDAQ
        """
        ticker = self.ticker
        url = "https://www.quandl.com/api/v3/datasets/EOD/" + ticker + ".json?api_key=2mDaZDV4cJgNjkzvf24u"
        response = requests.get(url)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def getRevAPI(self):
        """
        Ticker must be in CAPS
        ticker must be in NASDAQ
        """
        ticker = self.ticker
        url = "https://www.quandl.com/api/v3/datatables/SHARADAR/SF1.json?ticker=" + ticker + "&qopts.columns=ticker,dimension,datekey,revenue&api_key=2mDaZDV4cJgNjkzvf24u"
        response = requests.get(url)

        if response.status_code == 200:
          #  print(json.loads(response.content.decode('utf-8')))
            return json.loads(response.content.decode('utf-8'))
        else:
            return None
    def getRev(self):
        ticker = self.ticker
        API = self.RevAPI
        data = API["datatable"]["data"]
        total = 0
        Max = ""
        Rev = ""
        for i in data:
            if "2017" in i[2]:
                total += int(i[3])
            if i[2] > Max:
                Max = i[2]
                Rev = i[3]
      #  print(Rev)
        print("Total")
        print(total)
        return Rev

    def getVolume(self):
        ticker = self.ticker
        API = self.API
        dataset = API["dataset"]
        data = dataset["data"]
        mostRecent = data[0]
        volume = mostRecent[5]
        return volume

    def getDayPrice(self):
        """
        Return the most recent stock price for a given ticker
        :return:
        """
        ticker = self.ticker
        API = self.API
        dataset = API["dataset"]
        name = dataset["name"]
       # description = dataset["description"]
       # newestAvailableDate = dataset["newest_available_date"]
       # """
       # ["Date","Open","High","Low","Close","Volume","Dividend","Split","Adj_Open","Adj_High","Adj_Low","Adj_Close","Adj_Volume"]
       # """
        data = dataset["data"]
        mostRecent = data[0]
       # date = mostRecent[0]
        open = mostRecent[1]
       # volume = mostRecent[5]
       # dividend = mostRecent[6]


        # print ("newest_available_date:" + newestAvailableDate)
        return open



s = StockValue("MSFT")