from Plot_AQI import avg_data
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def met_data(month, year):   #func for scrapping html data as list
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()       #all text get stored in plain_text

    tempD = []
    finalD = []   #list for storing html data

    soup = BeautifulSoup(plain_text, "lxml")  #Beautiful Soup is a Python package for parsing HTML and XML documents
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):  #selecting class:'medias....' in table
        for tbody in table:   #html format contains tables,tbody
            for tr in tbody:   #extracting each row
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15      #anyway 15 cols r there, so diving total list/15 gives no of rows

    for times in range(round(rows)):   #iterarting through each row
        newtempD = []
        for i in range(15):  #15 cols(features) are there
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)  # finalD is a list having set of list

    length = len(finalD)

    finalD.pop(length - 1)#deleting 1st row that is not needed
    finalD.pop(0)           #deleting last row not needed

    for a in range(len(finalD)):  #removing unnecessary columns
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    print(mylist)
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2013, 2017):#iterarting through each year
        final_data = []         #new list to store avg of csv file and html data
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:  #if that file doesn't exist ,it will create one
            
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])  #giving col names
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp      #finala_data contains the whole year data at the end of for loop
            
        pm = avg_data(year)         #to get avg pm[2.5] value of that year

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in range(len(final_data)-1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
     
    total=data_2013+data_2014+data_2015+data_2016
    
    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
        
df=pd.read_csv('Data/Real-Data/Real_Combine.csv')