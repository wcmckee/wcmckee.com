
# coding: utf-8

# goodreasds

# In[1]:

import requests
import os
import getpass
import xmltodict
import arrow
import bs4
#import couchdb
#import nltk



# In[2]:

myusr = getpass.getuser()


# In[3]:

myusr


# In[18]:

para = {'key' : 'j6a7NN6aLyIGFrt9YHwibw', 'v': 2}


# In[19]:

getreview = requests.get('https://www.goodreads.com/review/list/5753105.xml', params = para)


# In[ ]:




# In[20]:

revxml = xmltodict.parse(getreview.text)


# In[21]:

print(revxml)


# In[22]:

bookdica = dict()


# In[23]:

for rev in range(20):
    bookdic = revxml['GoodreadsResponse']['reviews']['review'][rev]['book']
    
    #print(bookdic)
    print(bookdic['isbn'])
    print(bookdic['title'])
    bktit = bookdic['title_without_series']
    bknot = bktit.replace(' ', '-')
    bklow = bknot.lower()
    
    bookimg = bookdic['image_url']
    
    
    print(bklow)
    print(bookimg)
    print(bookdic['authors']['author']['name'])
    authimg = (bookdic['authors']['author']['image_url']['#text'])
    
    bkdes = (revxml['GoodreadsResponse']['reviews']['review'][rev]['book']['description'])
    soupdes = bs4.BeautifulSoup(bkdes)
    print(soupdes.text)
    #print(bookdic)
    #bookdic.update({bookdic['isbn'] : dict({'isbn' : bookdic['isbn'], 'slug' : bklow, 'autname' : bookdic['authors']['author']['name']})})#'autimg' : authimg, 'bookimg' : bookimg})})
    bookdica.update({str(bookdic['isbn']) : dict({'isbn' : bookdic['isbn'], 'num_pages' : bookdic['num_pages']})})
    pubday = (bookdic['publication_day'])
    pubmonth = (bookdic['publication_month'])
    pubyear = (bookdic['publication_year'])
    #pubyr = int(pubyear) + ',' + int(pubday) + ',' + int(pubmonth)
    try:
        ardate = arrow.get(int(pubyear), int(pubmonth), int(pubday))
        #print(pubday + ',' + pubmonth + ',' + pubyear)
        print(ardate)
        print(ardate.humanize())
        bookdic.update({bookdic : dict({'timestamp' : ardate, 'timehuman' : ardate.humanize()})})
    except TypeError:
        continue
    #print(bookdic['authors']['author'])
    #print(bookdic['authors']['author']['name'])
    
    

    print(bookdic['num_pages'])



# In[8]:

paraz = {'api-key' : '177948e7f058537298a9a57b29ac0195:11:74111394', 'list': 'e-book-fiction'}


# In[9]:

booklis = requests.get('https://api.nytimes.com/svc/books/v3/lists.json', params = paraz)


# In[10]:

bookjs = booklis.json()


# In[11]:

bookjs


# In[12]:

booklis = list()


# In[13]:

for bores in bookjs['results']:
    #for bor in bores:
    print(bores['book_details'])
    booklis.append(bores['book_details'])
    #print(bores['book_details'][0]['title'])
    #    print(bor)
    #print(bores['book_details'][bor]['author'])


# Get Goodreads book IDs given ISBNs
# Get Goodreads book IDs given one or more ISBNs. Response contains IDs without any markup.
# URL: https://www.goodreads.com/book/isbn_to_id    (sample url)
# HTTP method: GET
# Parameters:
# 
#     key: Developer key (required).
# 
#     isbn: ISBNs of books to look up.
# 
# 
# Get Goodreads work IDs g

# In[14]:

para = {'key' : 'j6a7NN6aLyIGFrt9YHwibw', 'v': 2}


# In[24]:

newsnip = dict()


# In[27]:

for bok in booklis:
    #print(bok)
    for bo in bok:
        #print(bo)
        print(bo)
        botit = (bo['title'])
        gifparm = {'q' : botit, 'api_key' : 'dc6zaTOxFJmzC'}
        reqgif = requests.get('http://api.giphy.com/v1/gifs/search', params = gifparm)
        print(reqgif.json())
        print(botit.capitalize())
        print(bo['description'])
        print(bo['author'])
        print(bo['publisher'])
        newdic = {'api-key' : '177948e7f058537298a9a57b29ac0195:11:74111394', 'q' : botit, 'sort' : 'newest'}
        newnews = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params = newdic)
        newsjs = (newnews.json())
        newdocs = newsjs['response']['docs']
        
        for newd in newdocs:
            print(newd)
            print(newd['headline']['print_headline'])
            newsnip.update({botit : dict({'printhead' : newd['headline']['print_headline'], 'snippet' : newd['snippet']})})
            print(newd['snippet'])

        #print(bo['primary_isbn13'])
        #print(bo['primary_isbn10'])
        #paraisb = {'key' : 'j6a7NN6aLyIGFrt9YHwibw', 'isbn': bo['primary_isbn13']}
        #reqgdr = requests.get('https://www.goodreads.com/book/isbn_to_id', params = paraisb)
        #print(reqgdr.text)
        #reqb = {'key' : 'j6a7NN6aLyIGFrt9YHwibw', 'q' : (bo['title'])}
        #reqsbib = requests.get('https://www.goodreads.com/search/index.xml', params = reqb)
        #print(reqsbib.text)


# In[49]:

newdic = {'api-key' : '177948e7f058537298a9a57b29ac0195:11:74111394', 'q' : 'blockchain', 'sort' : 'newest'}


# In[51]:

newnews = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params = newdic)


# In[53]:

newsjs = (newnews.json())


# In[57]:

newdocs = newsjs['response']['docs']


# In[62]:

for newd in newdocs:
    print(newd)
    print(newd['headline']['print_headline'])
    print(newd['snippet'])


# In[ ]:



