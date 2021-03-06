#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import re # import Regular expression operations module
import requests


# In[2]:


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


# In[3]:


url="https://www.amazon.in/Amazon-Brand-Solimo-Cotton-Paisley/dp/B06WLGNSVJ/ref=sr_1_2?dchild=1&pd_rd_r=3060fa4a-73de-4f2b-9812-78c75f40cc36&pd_rd_w=fSTQh&pd_rd_wg=MLYWo&pf_rd_p=a7129839-0ad8-4c89-831c-d9571786134f&pf_rd_r=FAWKGXA9FB329CNVRT6F&qid=1614973398&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-2"


# In[4]:


r = requests.get(url1, headers=headers)
soup = BeautifulSoup(r.content, "lxml")


# In[5]:


def get_title(soup):
 
    try:
        title = soup.find(id="productTitle").get_text().strip()
 
    except AttributeError:
        title = ""  
 
    return title


# In[ ]:





# In[7]:


def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price.split()[1]#.split()[1] for return string of price from bs4 string
 


# In[8]:





# In[9]:





# In[3]:





# In[ ]:




