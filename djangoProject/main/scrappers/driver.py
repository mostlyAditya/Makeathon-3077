from . import FLIPKART_SCRAPPER as fsc
from . import AMAZON_SCRAPPER as asc
from . import combine as com
# import AMAZON_SCRAPPER as asc
# import FLIPKART_SCRAPPER as fsc


def driver(link):
    # link = 'https://www.amazon.in/Amazon-Brand-Solimo-Cotton-Paisley/dp/B06WLGNSVJ/ref=sr_1_2?dchild=1&pd_rd_r=3060fa4a-73de-4f2b-9812-78c75f40cc36&pd_rd_w=fSTQh&pd_rd_wg=MLYWo&pf_rd_p=a7129839-0ad8-4c89-831c-d9571786134f&pf_rd_r=FAWKGXA9FB329CNVRT6F&qid=1614973398&refinements=p_n_format_browse-bin%3A19560802031&s=kitchen&sr=1-2'
    if 'www.amazon.in' in link:
        data_set1 = asc.pass_url(link)
        data_set2 = com.parent_scraper(['A', data_set1[0]])
        return [data_set1[0], data_set1[1], link, data_set2[0], data_set2[1], data_set2[2]]
        return asc.pass_url(link)
    elif 'www.flipkart.com' in link:
        data_set1 = fsc.pass_url(link)
        data_set2 = com.parent_scraper(['F', data_set1[0]])
        return [data_set2[0], data_set2[1], data_set2[2], data_set1[0], data_set1[1], link]

