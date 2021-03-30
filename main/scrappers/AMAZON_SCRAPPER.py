#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


def pass_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    # In[3]:

    # In[4]:

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    # In[5]:

    def get_title(soup):

        try:
            title = soup.find(id="productTitle").get_text().strip()

        except AttributeError:
            title = ""

        return title

    # In[7]:

    def get_price(soup):

        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()

        except AttributeError:
            price = ""

        return price.split()[1]  # .split()[1] for return string of price from bs4 string
    return [get_title(soup), get_price(soup), url]

