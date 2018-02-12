import json
import requests

class main():
    """
    Given a URL of an API endpoint, collect nodes and display valid and invalid menus
    """

    def __init__(self, jsonName, theURL):
        """
        dependency url ends in page number

        Initialize main searches through given URL to find valid and invalid menus
        :param jsonName: str   The name that the JSON file should be called, .txt not included.
        :param theURL: str     The URL of the endpoint
        """
        self.url = theURL
        self.noPage = self.url[:-1]
        API = self.getAPI(self.url)
        self.menus = []
        self.pagination = API["pagination"]
        self.totalPages = self.pagination["total"]
        self.children = []
        self.valid = True
        self.jsonName = jsonName

        #gather all endpoints
        for page in range(self.totalPages):

            page += 1 #pages start at 0 not 1


            newURL = self.noPage + str(page)
            API = self.getAPI(self.noPage + str(page))
            self.menus.extend(API["menus"])
        self.gatherChildren()


    def getAPI(self,aURL):
        """
        Returns content at url
        :param aURL: String   the URL
        :return: None or dict
        """
        response = requests.get(aURL)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def gatherChildren(self):
        """
        Return valid menus and invalid menus in a JSON file
        :return:
        """

        menus = self.menus
        #collect roots
        roots = []
        for id in menus:
            if not ('parent_id' in id):
                roots.append(id)
        #gather roots children
        finalData = {}

        for root in roots:
            self.checkForChildren(root)
            children = self.children
            self.children = []

            if not self.valid:
                children = children[:-1]
                if "invalid_menus" in finalData:
                    finalData["invalid_menus"].append({ "root_id": root["id"], "children": children })

                else:
                    finalData["invalid_menus"] = [{"root_id": root["id"], "children": children}]
                self.valid = True

            elif self.valid:
                if "valid_menus" not in finalData:
                    finalData["valid_menus"] = [{"root_id": root["id"], "children": children}]
                else:
                    finalData["valid_menus"].append({"root_id": root["id"], "children": children})
        print(finalData)
        with open(self.jsonName + '.txt', 'w') as outfile:
            json.dump(finalData, outfile)
        return finalData


    def checkForChildren(self, root):
        """
        Checks for children and collects them for the given root. Also identifies if valid or not
        :param root: dict
        :return: None
        """
        #base case
        if root["child_ids"] == []:
            return None
        #check if valid
        for child in root["child_ids"]:
            if child in self.children:
                self.valid = False
                return None
        #recursive case
        else:
            menus = self.menus
            for child in root['child_ids']:
                for id in menus:
                    if id['id'] == child:
                        self.children.append(child)
                        return  self.checkForChildren(id)




ch1 = main('ch1','https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1')
ch2 = main('ch2','https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&page=1')