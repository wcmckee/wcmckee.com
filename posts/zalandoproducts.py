
# coding: utf-8

# zalando products
# 
# analyze and extend the Zalando Products api
# 
# [{'activationDate': '2015-09-21T17:28:09+02:00', 'genders': ['MALE'], 'media': {'images': [{'thumbnailHdUrl': 'https://i3.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'largeUrl': 'https://i3.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'orderNumber': 1, 'type': 'NON_MODEL', 'largeHdUrl': 'https://i3.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'mediumUrl': 'https://i3.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'smallHdUrl': 'https://i3.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'smallUrl': 'https://i3.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg', 'mediumHdUrl': 'https://i3.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@14.jpg'}, {'thumbnailHdUrl': 'https://i2.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'largeUrl': 'https://i2.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'orderNumber': 2, 'type': 'STYLE', 'largeHdUrl': 'https://i2.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'mediumUrl': 'https://i2.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'smallHdUrl': 'https://i2.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'smallUrl': 'https://i2.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg', 'mediumHdUrl': 'https://i2.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@13.jpg'}, {'thumbnailHdUrl': 'https://i1.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'largeUrl': 'https://i1.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'orderNumber': 3, 'type': 'PREMIUM', 'largeHdUrl': 'https://i1.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'mediumUrl': 'https://i1.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'smallHdUrl': 'https://i1.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'smallUrl': 'https://i1.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg', 'mediumHdUrl': 'https://i1.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@12.jpg'}, {'thumbnailHdUrl': 'https://i4.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'largeUrl': 'https://i4.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'orderNumber': 4, 'type': 'PREMIUM', 'largeHdUrl': 'https://i4.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'mediumUrl': 'https://i4.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'smallHdUrl': 'https://i4.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'smallUrl': 'https://i4.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg', 'mediumHdUrl': 'https://i4.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@11.jpg'}, {'thumbnailHdUrl': 'https://i3.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'largeUrl': 'https://i3.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'orderNumber': 5, 'type': 'PREMIUM', 'largeHdUrl': 'https://i3.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'mediumUrl': 'https://i3.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'smallHdUrl': 'https://i3.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'smallUrl': 'https://i3.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg', 'mediumHdUrl': 'https://i3.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@10.jpg'}, {'thumbnailHdUrl': 'https://i1.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'largeUrl': 'https://i1.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'orderNumber': 6, 'type': 'PREMIUM', 'largeHdUrl': 'https://i1.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'mediumUrl': 'https://i1.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'smallHdUrl': 'https://i1.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'smallUrl': 'https://i1.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg', 'mediumHdUrl': 'https://i1.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@9.jpg'}, {'thumbnailHdUrl': 'https://i4.ztat.net/thumb_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'largeUrl': 'https://i4.ztat.net/large/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'orderNumber': 7, 'type': 'PREMIUM', 'largeHdUrl': 'https://i4.ztat.net/large_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'mediumUrl': 'https://i4.ztat.net/detail/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'smallHdUrl': 'https://i4.ztat.net/catalog_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'smallUrl': 'https://i4.ztat.net/catalog/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg', 'mediumHdUrl': 'https://i4.ztat.net/detail_hd/PI/92/2B/A0/4O/11/PI922BA04-O11@8.jpg'}]}, 'brand': {'key': 'PI9', 'shopUrl': 'https://www.zalando.co.uk/pier-one', 'name': 'Pier One', 'logoUrl': 'https://i5.ztat.net/brand/57b9e36b-7f6f-4bfd-8293-20984a3936ba.jpg', 'logoLargeUrl': 'https://i5.ztat.net/brandxl/57b9e36b-7f6f-4bfd-8293-20984a3936ba.jpg'}, 'season': 'WINTER', 'additionalInfos': [], 'tags': [], 'categoryKeys': ['catalog', 'men', 'mens-sale', 'mens-clothing-sale', 'mens-jackets-sale', 'all', 'sale', 'mens-clothing-jackets-suit-jackets-sale'], 'shopUrl': 'https://www.zalando.co.uk/pier-one-suit-jacket-brown-pi922ba04-o11.html', 'available': False, 'attributes': [{'values': ['100% polyester'], 'name': 'Lining'}, {'values': ['100% cotton'], 'name': 'Outer fabric material'}, {'values': ['button'], 'name': 'Fastening'}, {'values': ['27.5 " (Size M)'], 'name': 'Total length'}, {'values': ['Lapel collar'], 'name': 'Collar'}, {'values': ['17.0 " (Size M)'], 'name': 'Back width'}, {'values': ['standard'], 'name': 'Length'}, {'values': ['Inside pockets'], 'name': 'Pockets'}, {'values': ['tailored'], 'name': 'Fit'}, {'values': ['Herringbone'], 'name': 'Pattern'}, {'values': ['Dry clean only'], 'name': 'Washing instructions'}, {'values': ['long', '26.0 " (Size M)'], 'name': 'Sleeve length'}, {'values': ['Our model is 73.0 " tall and is wearing size M'], 'name': "Our model's height"}], 'units': [{'available': False, 'size': 'XL', 'originalPrice': {'value': 59.99, 'currency': 'GBP', 'formatted': '£59.99'}, 'id': 'PI922BA04-O1100XL000', 'stock': 0, 'price': {'value': 30.0, 'currency': 'GBP', 'formatted': '£30.00'}}, {'available': False, 'size': 'L', 'originalPrice': {'value': 59.99, 'currency': 'GBP', 'formatted': '£59.99'}, 'id': 'PI922BA04-O11000L000', 'stock': 0, 'price': {'value': 30.0, 'currency': 'GBP', 'formatted': '£30.00'}}, {'available': False, 'size': 'M', 'originalPrice': {'value': 59.99, 'currency': 'GBP', 'formatted': '£59.99'}, 'id': 'PI922BA04-O11000M000', 'stock': 0, 'price': {'value': 30.0, 'currency': 'GBP', 'formatted': '£30.00'}}, {'available': False, 'size': 'XXL', 'originalPrice': {'value': 59.99, 'currency': 'GBP', 'formatted': '£59.99'}, 'id': 'PI922BA04-O1102XL000', 'stock': 0, 'price': {'value': 30.0, 'currency': 'GBP', 'formatted': '£30.00'}}, {'available': False, 'size': 'S', 'originalPrice': {'value': 59.99, 'currency': 'GBP', 'formatted': '£59.99'}, 'id': 'PI922BA04-O11000S000', 'stock': 0, 'price': {'value': 30.0, 'currency': 'GBP', 'formatted': '£30.00'}}], 'modelId': 'PI922BA04', 'seasonYear': '2015', 'id': 'PI922BA04-O11', 'ageGroups': ['ADULT'], 'name': 'Suit jacket - brown', 'color': 'Brown'}

# In[23]:

import requests
import getpass
import arrow
import json
from urllib.parse import urlparse
from IPython.display import Image
from nltk.tag import pos_tag
import nltk

import PIL


# In[2]:

myusr = getpass.getuser()


# In[3]:

myusr


# In[4]:

curtim = arrow.now()


# In[5]:

str(curtim)


# In[6]:

#prodreq = requests.get('https://api.zalando.com/articles')


# In[7]:

#prodjsn = prodreq.json()


# In[8]:

#prodjsn['totalPages']


# In[9]:

#dicprods = dict()


# In[10]:

'''
for totp in range(1, 5):
    print(totp)
    prodreq = requests.get('https://api.zalando.com/articles?page={}'.format(totp))
    pror = (prodreq.json())
    #print('https://api.zalando.com/articles?page={}'.format(str(totp)))
    #print(pror['content'])
    
    lencon = len(pror['content'])
    
    for lenc in range(0, lencon):
        
        print(pror['content'][lenc]['name'])
        
        #print(pror['content'][lenc])
        
        for myuni in (pror['content'][lenc]['units']):
            print(myuni['size'])
            print(myuni['price']['value'])
            print(myuni['price']['currency'])
            
            print(myuni['originalPrice']['value'])
            print(myuni['originalPrice']['value'])
            print(myuni['id'])
        #print(pror['content'][lenc])
        
           
        braur = (pror['content'][lenc]['brand']['shopUrl'])
        brpars = urlparse(braur)
        brpah = brpars[2]
        potitle = (brpah.replace('/', ''))
        print(potitle)
        
        prlen = len(pror['content'][lenc]['media']['images'])
        for prl in range(0, prlen):
            #print(pror['content'][lenc]['media']['images'][prl])
            imgno = (pror['content'][lenc]['media']['images'][prl]['largeUrl'])
            
            with open('/home/{}/za/posts/{}.md'.format(myusr, potitle), 'a') as zamd:
                zamd.write(('![' + potitle + '](' + imgno + ')\n\n'))
                
            with open ('/home/{}/za/posts/{}.meta'.format(myusr, potitle), 'w') as opmetat:
            #opmetat.write("{}".format(str(curtim))
                opmetat.write('.. title: {}\n.. slug: {}\n.. date: {}\n.. tags: \n.. link:\n.. description:\n.. type: text'.format(potitle, potitle, curtim))


        dicprods.update({potitle : 'hello'})
        #print(prlen)
        #pror['content']
'''


# In[11]:

reqgli = requests.get('https://api.gilt.com/v1/sales/active.json?apikey=bb7cf716ec52e7a7737705f0129ed4282a35239a0a6b8a821e68f30a00ecc1a7')


# In[12]:

glijs = reqgli.json()


# In[13]:

glisale = glijs['sales']


# In[14]:

lenmgio = len(glisale)


# In[15]:

lenmgio


# {'products': ['https://api.gilt.com/v1/products/1167852275/detail.json', 'https://api.gilt.com/v1/products/1167852274/detail.json', 'https://api.gilt.com/v1/products/1167852280/detail.json', 'https://api.gilt.com/v1/products/1167868671/detail.json', 'https://api.gilt.com/v1/products/1174473877/detail.json', 'https://api.gilt.com/v1/products/1167852271/detail.json', 'https://api.gilt.com/v1/products/1171175079/detail.json', 'https://api.gilt.com/v1/products/1178062369/detail.json', 'https://api.gilt.com/v1/products/1178061681/detail.json', 'https://api.gilt.com/v1/products/1174473883/detail.json', 'https://api.gilt.com/v1/products/1178062134/detail.json', 'https://api.gilt.com/v1/products/1145478683/detail.json', 'https://api.gilt.com/v1/products/1174473893/detail.json', 'https://api.gilt.com/v1/products/1145857261/detail.json', 'https://api.gilt.com/v1/products/1145857254/detail.json', 'https://api.gilt.com/v1/products/1145216323/detail.json', 'https://api.gilt.com/v1/products/1145857267/detail.json', 'https://api.gilt.com/v1/products/1174473872/detail.json', 'https://api.gilt.com/v1/products/1145857278/detail.json', 'https://api.gilt.com/v1/products/1174473895/detail.json', 'https://api.gilt.com/v1/products/1175595234/detail.json', 'https://api.gilt.com/v1/products/1145857270/detail.json', 'https://api.gilt.com/v1/products/1174473899/detail.json', 'https://api.gilt.com/v1/products/1174473881/detail.json', 'https://api.gilt.com/v1/products/1174473897/detail.json', 'https://api.gilt.com/v1/products/1178062378/detail.json', 'https://api.gilt.com/v1/products/1178060678/detail.json', 'https://api.gilt.com/v1/products/1178062404/detail.json', 'https://api.gilt.com/v1/products/1174018873/detail.json', 'https://api.gilt.com/v1/products/1174018845/detail.json', 'https://api.gilt.com/v1/products/1178062413/detail.json', 'https://api.gilt.com/v1/products/1174018848/detail.json', 'https://api.gilt.com/v1/products/1174018867/detail.json', 'https://api.gilt.com/v1/products/1178062390/detail.json', 'https://api.gilt.com/v1/products/1174018856/detail.json', 'https://api.gilt.com/v1/products/1145857257/detail.json', 'https://api.gilt.com/v1/products/1174018898/detail.json', 'https://api.gilt.com/v1/products/1149852189/detail.json', 'https://api.gilt.com/v1/products/1149852191/detail.json', 'https://api.gilt.com/v1/products/1174018860/detail.json', 'https://api.gilt.com/v1/products/1173925652/detail.json', 'https://api.gilt.com/v1/products/1149852175/detail.json', 'https://api.gilt.com/v1/products/1144742378/detail.json', 'https://api.gilt.com/v1/products/1144742374/detail.json', 'https://api.gilt.com/v1/products/1145478739/detail.json', 'https://api.gilt.com/v1/products/1173623626/detail.json', 'https://api.gilt.com/v1/products/1145857274/detail.json', 'https://api.gilt.com/v1/products/1168300716/detail.json', 'https://api.gilt.com/v1/products/1160299290/detail.json', 'https://api.gilt.com/v1/products/1174473904/detail.json', 'https://api.gilt.com/v1/products/1174473902/detail.json', 'https://api.gilt.com/v1/products/1145857264/detail.json', 'https://api.gilt.com/v1/products/1173508014/detail.json', 'https://api.gilt.com/v1/products/1174473866/detail.json', 'https://api.gilt.com/v1/products/1174018900/detail.json', 'https://api.gilt.com/v1/products/1174018871/detail.json', 'https://api.gilt.com/v1/products/1145857262/detail.json', 'https://api.gilt.com/v1/products/1145857256/detail.json', 'https://api.gilt.com/v1/products/1174473915/detail.json', 'https://api.gilt.com/v1/products/1145857266/detail.json', 'https://api.gilt.com/v1/products/1174473888/detail.json', 'https://api.gilt.com/v1/products/1169364216/detail.json', 'https://api.gilt.com/v1/products/1178062383/detail.json', 'https://api.gilt.com/v1/products/1171174582/detail.json', 'https://api.gilt.com/v1/products/1171174868/detail.json', 'https://api.gilt.com/v1/products/1174473876/detail.json', 'https://api.gilt.com/v1/products/1169364124/detail.json', 'https://api.gilt.com/v1/products/1169364167/detail.json', 'https://api.gilt.com/v1/products/1149852159/detail.json', 'https://api.gilt.com/v1/products/1171190539/detail.json', 'https://api.gilt.com/v1/products/1174018858/detail.json', 'https://api.gilt.com/v1/products/1174018971/detail.json', 'https://api.gilt.com/v1/products/1169364211/detail.json', 'https://api.gilt.com/v1/products/1174018852/detail.json', 'https://api.gilt.com/v1/products/1175598415/detail.json', 'https://api.gilt.com/v1/products/1174473864/detail.json', 'https://api.gilt.com/v1/products/1144742367/detail.json', 'https://api.gilt.com/v1/products/1174473879/detail.json', 'https://api.gilt.com/v1/products/1144742376/detail.json', 'https://api.gilt.com/v1/products/1149698672/detail.json', 'https://api.gilt.com/v1/products/1171174040/detail.json', 'https://api.gilt.com/v1/products/1174473890/detail.json', 'https://api.gilt.com/v1/products/1174018901/detail.json', 'https://api.gilt.com/v1/products/1145857250/detail.json', 'https://api.gilt.com/v1/products/1145216309/detail.json', 'https://api.gilt.com/v1/products/1145216362/detail.json', 'https://api.gilt.com/v1/products/1171070525/detail.json', 'https://api.gilt.com/v1/products/1169364163/detail.json', 'https://api.gilt.com/v1/products/1169364151/detail.json', 'https://api.gilt.com/v1/products/1145857279/detail.json', 'https://api.gilt.com/v1/products/1178062055/detail.json', 'https://api.gilt.com/v1/products/1174018903/detail.json', 'https://api.gilt.com/v1/products/1145216306/detail.json', 'https://api.gilt.com/v1/products/1144742370/detail.json', 'https://api.gilt.com/v1/products/1144742372/detail.json', 'https://api.gilt.com/v1/products/1122483386/detail.json', 'https://api.gilt.com/v1/products/1145857260/detail.json', 'https://api.gilt.com/v1/products/1175595608/detail.json', 'https://api.gilt.com/v1/products/1174473910/detail.json', 'https://api.gilt.com/v1/products/1174473908/detail.json'], 'sale': 'https://api.gilt.com/v1/sales/men/billy-reid-1406/detail.json', 'name': 'New Arrivals: Apparel', 'sale_url': 'http://www.gilt.com/sale/men/billy-reid-1406?utm_medium=api&utm_source=salesapi', 'begins': '2017-01-12T17:00:00Z', 'sale_key': 'billy-reid-1406', 'store': 'men', 'ends': '2017-01-15T17:00:00Z', 'description': 'Everyday essentials you’ll turn to again and again', 'image_urls': {'253x137': [{'height': 137, 'width': 253, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748852/orig.jpg'}], '940x280': [{'height': 280, 'width': 940, 'url': ''}], '636x400': [{'height': 400, 'width': 636, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0975/509751438/orig.jpg'}], '468x437': [{'height': 437, 'width': 468, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748865/orig.jpg'}], '1536x640': [{'height': 640, 'width': 1536, 'url': ''}], '140x130': [{'height': 130, 'width': 140, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748849/orig.jpg'}], '1024x320': [{'height': 320, 'width': 1024, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748848/orig.jpg'}], '676x686': [{'height': 686, 'width': 676, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748873/orig.jpg'}], '768x320': [{'height': 320, 'width': 768, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748875/orig.jpg'}], '468x652': [{'height': 652, 'width': 468, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748866/orig.jpg'}], '308x330': [{'height': 330, 'width': 308, 'url': ''}], '385x173': [{'height': 173, 'width': 385, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748863/orig.jpg'}], '590x213': [{'height': 213, 'width': 590, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748844/orig.jpg'}], '161x110': [{'height': 110, 'width': 161, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748845/orig.jpg'}], '744x281': [{'height': 281, 'width': 744, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748879/orig.jpg'}], '620x280': [{'height': 280, 'width': 620, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748870/orig.jpg'}], '255x195': [{'height': 195, 'width': 255, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748855/orig.jpg'}], '100x93': [{'height': 93, 'width': 100, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748847/orig.jpg'}], '455x172': [{'height': 172, 'width': 455, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0975/509751330/orig.jpg'}], '343x187': [{'height': 187, 'width': 343, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748860/orig.jpg'}], '80x85': [{'height': 85, 'width': 80, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748876/orig.jpg'}], '315x295': [{'height': 295, 'width': 315, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748858/orig.jpg'}], '185x173': [{'height': 173, 'width': 185, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748851/orig.jpg'}], '624x668': [{'height': 668, 'width': 624, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748871/orig.jpg'}], '320x153': [{'height': 153, 'width': 320, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748878/orig.jpg'}], '650x280': [{'height': 280, 'width': 650, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0975/509751586/orig.jpg'}], '686x374': [{'height': 374, 'width': 686, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748874/orig.jpg'}], '940x652': [{'height': 652, 'width': 940, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748877/orig.jpg'}], '612x526': [{'height': 526, 'width': 612, 'url': ''}], '466x247': [{'height': 247, 'width': 466, 'url': ''}], '490x250': [{'height': 250, 'width': 490, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748884/orig.jpg'}], '506x274': [{'height': 274, 'width': 506, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748867/orig.jpg'}], '300x280': [{'height': 280, 'width': 300, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748857/orig.jpg'}], '287x195': [{'height': 195, 'width': 287, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748846/orig.jpg'}], '2048x640': [{'height': 640, 'width': 2048, 'url': ''}], '253x260': [{'height': 260, 'width': 253, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748853/orig.jpg'}], '468x211': [{'height': 211, 'width': 468, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748864/orig.jpg'}], '2544x1344': [{'height': 1344, 'width': 2544, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748854/orig.jpg'}], '338x343': [{'height': 343, 'width': 338, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748859/orig.jpg'}], '645x295': [{'height': 295, 'width': 645, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748872/orig.jpg'}], '366x186': [{'height': 186, 'width': 366, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748886/orig.jpg'}], '240x163': [{'height': 163, 'width': 240, 'url': ''}], '1264x1352': [{'height': 1352, 'width': 1264, 'url': ''}], '375x195': [{'height': 195, 'width': 375, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748862/orig.jpg'}], '370x345': [{'height': 345, 'width': 370, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748861/orig.jpg'}], '506x520': [{'height': 520, 'width': 506, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748869/orig.jpg'}], '300x184': [{'height': 184, 'width': 300, 'url': 'https://cdn1.gilt.com/images/share/uploads/0000/0005/0974/509748856/orig.jpg'}]}, 'size': 100}

# In[16]:

thesales = dict()


# In[17]:

#womensales = dict()


# In[18]:

#kidsales = dict()


# In[ ]:

for glis in range(0, lenmgio):
    #print(glisale[glis])
    glikey = (glisale[glis]['sale_key'])
    
    #print(glisale[glis]['description'])
    
    print(glisale[glis]['image_urls']['506x520'][0]['url'])
    gliyurl = (glisale[glis]['image_urls']['506x520'][0]['url'])
    try:
        gliprod = (glisale[glis]['products'])
        for glip in gliprod:
            glpass = (glip + '?apikey=bb7cf716ec52e7a7737705f0129ed4282a35239a0a6b8a821e68f30a00ecc1a7')
            print(glpass)
            reqprod = requests.get(glpass)


            reqjs = reqprod.json()
            print(reqprod.json())



            print(reqjs['brand'])

            print(reqjs['name'])

            print(reqjs['url'])

            brpars = urlparse(reqjs['url'])
            brpah = brpars[2]
            brtitle = brpah.replace('/', '')
            print(brtitle)

            print(reqjs['content'])

            #print(reqjs['description'])

            thesales.update({(glisale[glis]['sale_key']) : dict({'name' : glisale[glis]['name'], 
                                                                 'description' : glisale[glis]['description'],
                                                                 'imgurl' : gliyurl, 'key' : glikey,
                                                                    glis : brtitle, 'store': glisale[glis]['store']})})

            #if (glisale[glis]['store']) == 'women':
            #    womensales.update({(glisale[glis]['sale_key']) : dict({'name' : glisale[glis]['name'], 
            #                                                     'description' : glisale[glis]['description'],
            #                                                     'imgurl' : gliyurl, 'key' : glikey,
            #                                                          glis : brtitle})})
            #    
            #if (glisale[glis]['store']) == 'kids':
            #    kidsales.update({(glisale[glis]['sale_key']) : dict({'name' : glisale[glis]['name'], 
            #                                                     'description' : glisale[glis]['description'],
            #                                                     'imgurl' : gliyurl, 'key' : glikey,
            # glis : brtitle})})
            
    except KeyError:
        pass



# In[25]:

saledump = json.dumps(thesales)


# In[27]:

with open('/home/{}/giltsale.json'.format(myusr), 'w') as gilsal:
    gilsal.write(saledump)


# In[ ]:

#wokey = womensales.keys()


# In[ ]:

#deslis = list()


# In[ ]:

#for wom in wokey:
#    print(womensales[wom]['description'])
#    deslis.append(womensales[wom]['description'])
#    print(womensales[wom])
#    print(womensales[wom]['imgurl'])


# In[ ]:

#imgmreq = requests.get(womensales[wom]['imgurl'])


# In[ ]:

#imgmreq


# In[ ]:

#response = requests.get(url, stream=True)
#        with open('{}{}-reference.jpg'.format(repathz, str(rdz.author)), 'wb') as out_file:
#           shutil.copyfileobj(response.raw, out_file)
#            del response


# In[162]:

#Image(womensales[wom]['imgurl'])


# In[124]:

#myblog = ' '.join(deslis)


# In[126]:

#tokens = nltk.word_tokenize(myblog)


# In[130]:

#setok = set(tokens)


# In[128]:

#from nltk.tag import pos_tag


# In[132]:

#post = pos_tag(setok)#


# In[133]:

#post


# In[136]:

#rbword = [word for word,pos in post if pos == 'RB']

#nnword = [word for word,pos in post if pos == 'NN']


# In[101]:

#lenlen = len(mensales)


# In[92]:

'''
with open('/home/{}/glitprod.json'.format(myusr), 'r') as glpro :
    #print(glpro.read())
    glrd = (json.loads(glpro.read()))
    prosku =(glrd['skus'])
    lenpro = (len(prosku[0]))
    try:
        for lenp in range(0, lenpro):
            #print(prosku[lenp])
            #print(prosku[lenp]['attributes'])
            
            #print (prosku[lenp]['attributes'][0])
            
            print (prosku[lenp]['attributes'][1]['value'])
            
            
            #print (prosku[lenp]['attributes'][1]['msrp_price'])
            
            #print (prosku[lenp]['attributes'][1]['sale_price'])
    except IndexError:
        pass
    print(glrd['id'])
    for glca in (glrd['categories']):
        print(glca)
    print(glrd['categories'])
    print(glrd)
    print(glrd['url'])
    brpars = urlparse(glrd['url'])
    brpah = brpars[2]
    brtitle = (brpah.replace('/', ''))
    print(brtitle)
'''

