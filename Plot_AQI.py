import pandas as pd
import matplotlib.pyplot as plt
import sys



    
def avg_data(a ):
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi{}.csv'.format(a),chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    

    

if __name__=="__main__":
    #i=0
    #pm=[]
    
    for year in range(2013,2018):
        lst_data=0
        lst_data = avg_data(year)
       # pm.append(lst_data)
        if year ==2014:
            plt.plot(range(0,364),lst_data,label="2014 data")
        else:
            plt.plot(range(0,365),lst_data,label="{} data".format(year))
       # i+=1
        

            

            
    #lst2013=avg_data_2013()
    #lst2014=avg_data_2014()
    #lst2015=avg_data_2015()
    #lst2016=avg_data_2016()
    #lst2017=avg_data_2017()
    #lst2018=avg_data_2018()
    
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
	




