from shareplum import Site
from requests_ntlm import HttpNtlmAuth

cred = HttpNtlmAuth('idmgtsupport@nibss-plc.com.ng', 'ID$$12345')
site = Site('https://nibssng.sharepoint.com/sites/IDENTITYMANAGEMENTOPERATIONS', auth=cred)
sp_list = site.List('BTSS')

list_data = sp_list.GetListItems()