import os  
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.listitems.caml.caml_query import CamlQuery 

SP_SITE_URL ='https://trainingcenter2021.sharepoint.com/sites/ABC/'
SP_DOC_LIBRARY ='Publications'
SP_DOC_LIBRARY_FOLDER ='Administrator'
# The folder in the document library 
USERNAME ='sptraining@trainingcenter2021.onmicrosoft.com'
PASSWORD ='******' 

# 1. Assuming the location of the uploading file 
file_path ="C:/temp/administration/Request Form2.docx" 
file_name =os.path.basename(file_path)

# 2. Create a ClientContext object to access the SharePoint library 
ctx =ClientContext(SP_SITE_URL).with_user_credentials(USERNAME, PASSWORD) 

# 3. Access the SharePoint folder or create the folder if it doesn’t exist 
sp_folder_path ="/{0}/{1}".format(SP_DOC_LIBRARY,SP_DOC_LIBRARY_FOLDER)
sp_folder  =  ctx.web.ensure_folder_path(sp_folder_path).execute_query()

# 4. Read the content of the file 
with open(file_path,'rb')as file_obj: 
  file_content = file_obj.read()

# 5. Upload the file to the folder in the SharePoint library 
sp_file = sp_folder.upload_file(file_name, file_content) 
ctx.execute_query()

# 6. Add metadata to the uploaded document 
item = sp_file.listItemAllFields 
item.set_property("Category","Form")
item.update()
ctx.execute_batch()