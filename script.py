#!/usr/bin/env python
# coding: utf-8

# # Initialization

# In[1]:


import configparser
import socket
import subprocess


# # Define and Fetch Variables.

# In[2]:


config = configparser.RawConfigParser()
config.read('config.ini')
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


# # Prepare

# In[3]:


value = 'DEFAULT'
DCTYPE = config.get(hostname, 'DCTYPE', raw=False)
REGION = config.get(hostname, 'REGION', raw=False)
print(DCTYPE)  # -> "Python is fun!"

print('The Script will run from Host:[',hostname,'][',ip_address,'], Deployment Type[',DCTYPE,']', ' in the region:[',REGION,']')

subprocess.call(["../test-project/shell.sh"])

command = '../test-project/shell.sh'
exitvalue = subprocess.call([command])
print(exitvalue)

# In[ ]:




