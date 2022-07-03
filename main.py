from sharepoint import SharePoint
import datetime  
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
days = datetime.timedelta(1)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y%m%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 

#i.e - file_dir_path = r'C:\project\report.pdf'
file_dir_path = r'C:\python_work\webservice_monitor\status.csv'
 
# this will be the file name that it will be saved in SharePoint as 
file_name = 'status.csv'

# The folder in SharePoint that it will be saved under
folder_name = 'BTSS'

# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# delete file
#SharePoint().delete_file(file_name, folder_name)