from googlesearch import search
import AMAZON_SCRAPPER as asc
import FLIPKART_SCRAPPER as fsc


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def searchIt(site_name, title):
    if site_name == "A":
        query = title + "Flipkart"



    elif site_name == "F":
        query = title + "Amazon"

    url_link = [x for x in search(query, tld="co.in", num=1, stop=0, pause=2)]
    print(len(url_link))
    #print(url_link)



searchIt("A", "Sparx Men's Sd0323g Sneakers")




