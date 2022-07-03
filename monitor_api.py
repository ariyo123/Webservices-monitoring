import os
from unittest import result
import requests
import csv
import datetime
import pandas
import time
i = 1
while i < 6:
  
#from datetime import date, timedelta
    import time
    print("\n\n\n\n")
    print("you're about to see the status of your webservices")
    #get current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    #get cureent date
    CurrentDate=datetime.date.today()  
    days = datetime.timedelta(0)

    new_date = CurrentDate - days
    final_date= new_date.strftime('%Y-%m-%d')
    #%d is for date  
    #%m is for month  
    #Y is for Year  
    print(final_date) 

    os.remove("status.csv")

    result1=[]
    #calling the webservices dictionary to confirm the status
    BASE_URL = {
        'service1':'https://fakestoreapi.com',
        #'service2':'https://fakestoreapi.com/1',
        'service3':'https://api.github.com/users/defunkt'
    }
    #calling the webservices dictionary to confirm the status
    for key, value in BASE_URL.items():
            response = requests.get(f"{value}")
            #result = response.json()
            result2 = response.status_code
            result=f'Status of {value} ({key})  is {result2} as at {final_date} {current_time}'
            result1.append(result)
            
            print(result.split('\n'))
            
            with open('status.csv', 'a', newline='') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ' ')
                #final_result=result1.split('\n')

                my_writer.writerow('')
                my_writer.writerow(result.split())
                
                csvfile.close()

        
    print("\n\n")


    file = pandas.read_csv("status.csv")
    file.to_html("webservice_status.html")
    time.sleep(300)
print(i)
i += 1
