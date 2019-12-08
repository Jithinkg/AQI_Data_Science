import os     
import time   #time taken to extract all html files
import requests   #download that part. webpage in form of html
import sys

def retrieve_html():
    for year in range(2013,2019):  #to collect data from 2013 to 2018
        for month in range(1,13):  #for 12 month 
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
				#{}- will be replaced with format()
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url)   #req.get function to retrieve	 all text
            text_utf=texts.text.encode('utf=8')  #utf encoding
            
            if not os.path.exists("Data/Html_Data/{}".format(year)): #check whether`"Data/Html_Data/{}".format(year) is present
                os.makedirs("Data/Html_Data/{}".format(year))  # if not ,make one using os.makedirs
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:  #for opening that file
                output.write(text_utf)  #write the encoded html to that path file
            
        sys.stdout.flush()
		
if __name__=="__main__":    #main function
    start_time=time.time()
    retrieve_html()    # calling 'retrieve fn' to get html files
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))