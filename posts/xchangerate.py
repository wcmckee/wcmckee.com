
# coding: utf-8

# # reserve bank exchange rate
# 
# downloads excel file from rbnz. Saves to to local file system. Convert content to json and serve. 

# In[1]:

import xmltodict
import requests
import shutil
import getpass
import arrow
import pandas
import json


# In[43]:

myusr = getpass.getuser()


# In[44]:

reqdaily = requests.get('http://www.rbnz.govt.nz/-/media/ReserveBank/Files/Statistics/tables/b1/hb1-daily.xls', stream=True)


# In[45]:

usrpat = '/home/{}'.format(myusr)


# In[46]:

#import requests
#dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
#resp = requests.get(dls)
with open('{}/daily.xls'.format(usrpat), 'wb') as output:
    output.write(reqdaily.content)


# In[49]:

dailyrd = pandas.read_excel('{}/daily.xls'.format(usrpat), header=1, index_col=0, skiprows=[2,3,4])


# In[53]:

tojsn = dailyrd.to_json()


# In[55]:

jsz = json.loads(tojsn)


# In[41]:

with open('/home/{}/artctrl/exchange.json'.format(myusr), 'w') as exchan:
          exchan.write(str(jsz))

          

