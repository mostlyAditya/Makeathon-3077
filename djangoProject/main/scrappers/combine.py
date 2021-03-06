from googlesearch import search
from . import AMAZON_SCRAPPER as asc
from . import FLIPKART_SCRAPPER as fsc
# import AMAZON_SCRAPPER as asc
# import FLIPKART_SCRAPPER as fsc


def parent_scraper(details):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    def searchIt(site_name, title):
        if site_name == "A":
            query = title + "Flipkart"

        elif site_name == "F":
            query = title + "Amazon"

        url_link = [x for x in search(query, tld="co.in", num=1, stop=1, pause=2)]
        result = None
        if site_name == 'A':
            result = fsc.pass_url(url_link[0])
        elif site_name == 'F':
            result = asc.pass_url(url_link[0])
        return [result[0], result[1], url_link[0]]

    return searchIt(details[0], details[1])




