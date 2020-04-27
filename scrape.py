import re

import re
class extractData:
    def __init__(self, table):
        self.table = table
        #separating table data into three sections
        self.table1 = table[0].find_all('td')
        self.table2 = table[1].find_all('td')
        self.table3 = table[2].find_all('td')
        self.table4 = table[3].find_all('th')
        self.table5 = table[3].find_all('td')
    
    def getDriverDetails(self, tableDetailsList):
        details = dict()
        for i in range(0,len(tableDetailsList),2): #increment by 2 since column 2 has content and column 1 has what content it is for
            #re.sub to remove extra whitespaces in name
            details[tableDetailsList[i].text[:-1]] = (re.sub(' +', ' ', tableDetailsList[i+1].text))
        return details
    
    def getValidity(self, tableDetailsList1, tableDetailsList2):
        details = dict()
        for i in range(0,len(tableDetailsList1),3):
            From = tableDetailsList1[i+1].text[5:]
            To = tableDetailsList1[i+2].text[3:]
            details[tableDetailsList1[i].text] = {"from": From, "to": To}
        for i in range(0,len(tableDetailsList2),2):
            details[tableDetailsList2[i].text[:-1]] = tableDetailsList2[i+1].text
        return details
    
    def getCOV(self, tableHeaderList, tableDataList):
        finalDetails = list() #creating list since there can be many class of vehicles for a person
        for i in range(0,len(tableDataList),3):
            details = dict()
            details[tableHeaderList[0].text] = tableDataList[i].text
            details[tableHeaderList[1].text] = tableDataList[i+1].text
            details[tableHeaderList[2].text] = tableDataList[i+2].text
            finalDetails.append(details)
        return finalDetails
    
    def getJSON(self): # method to return final json
        json = dict()
        json['Driver Details'] = self.getDriverDetails(self.table1)
        json['Validity'] = self.getValidity(self.table2, self.table3)
        json['Class Of Vehicle'] = self.getCOV(self.table4, self.table5)
        return json