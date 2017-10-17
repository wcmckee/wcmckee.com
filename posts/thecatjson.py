
# coding: utf-8

# The Cat Json
# 
# Returns json result of random cat images instead of xml

# In[26]:


import json
import requests
import xmltodict
from flask import Flask, jsonify
from flask_restful import Resource, Api
import random


# In[27]:


app = Flask(__name__)
api = Api(app)


# In[28]:


catreq = (requests.get('http://thecatapi.com/api/images/get?format=xml&results_per_page=50'))


# In[29]:


catxt = catreq.text


# In[30]:


catdict = xmltodict.parse(catxt)


# In[31]:


caim = catdict['response']['data']['images']['image']


# In[32]:


class HelloWorld(Resource):
    def get(self):
        jsdump = caim[random.randint(0,49)]

        return (json.loads(json.dumps(jsdump)))


# In[33]:


api.add_resource(HelloWorld, '/')


# In[34]:


if __name__ == '__main__':
    app.run(debug=True)

