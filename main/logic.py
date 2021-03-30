import urllib.request
import bs4
import re

def get_amazon_results():
    htmltext = urllib.request.urlopen('https://amazon.in')
    return (bs4.BeautifulSoup(str(htmltext.read()), 'html.parser').find('body'))

