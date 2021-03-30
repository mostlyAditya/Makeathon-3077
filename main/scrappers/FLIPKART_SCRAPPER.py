#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


def pass_url(url):
    # In[2]:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    # In[3]:

    # url="https://www.flipkart.com/realme-narzo-20-pro-white-knight-64-gb/p/itm043c480bf22fb?pid=MOBFVEATHFZNHMWU&lid=LSTMOBFVEATHFZNHMWUB82QVN&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3AMOBFPCX72FRDVFKB%3Bpt%3Ahp%3Buid%3A0bcc3c6b-7dec-11eb-8873-137b9bb0a7bc%3B.MOBFVEATHFZNHMWU&ppt=clp&ppn=mobile-phones-store&ssid=n5bnr871280000001614973712668&otracker=hp_reco_Suggested%2Bfor%2BYou_3_9.productCard.PMU_V2_Realme%2BNarzo%2B20%2BPro%2B%2528White%2BKnight%252C%2B64%2BGB%2529_MOBFVEATHFZNHMWU_personalisedRecommendation%2Fp2p-same_2&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_Suggested%2Bfor%2BYou_DESKTOP_HORIZONTAL_productCard_cc_3_NA_view-all&cid=MOBFVEATHFZNHMWU"

    # In[4]:

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    # In[6]:

    def get_title(soup):

        try:
            title = soup.find('span', attrs={'class': 'B_NuCI'})

        except AttributeError:
            title = ""

        return title.text

    def get_price(soup):

        try:
            price = soup.find("div", attrs={'class': '_30jeq3 _16Jk6d'}).string.strip()

        except AttributeError:
            price = ""

        return price.split()[0]  # .split()[0] for return string of price from bs4 string

    return [get_title(soup), get_price(soup)]


