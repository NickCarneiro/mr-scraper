# searches Bing for given string, evaluates pages and returns a list of valid sources
from bing_search_api import BingSearchAPI
import time
def search_bing(query, per_page=10, offset=0):
    try:
        my_key = ""
        bing = BingSearchAPI(my_key)
        params = {'$format': 'json',
                  '$top': per_page,
                  '$skip': offset}
        results = bing.search('image+web', query, params)
        results = results['d']['results'][0]['Web']
        return results
    except(e):
        print e
        return []

def save_source_urls():
    f = open('source_urls.data', 'w')

    desired_results = 100
    i = 0
    while i < desired_results:
        print 'searching with offset %d' % i
        results = search_bing("Powered By IP.Board", 10, i)
        for result in results:
            f.write(result['Url'] + '\n')
            print result['Url']
        i += 10
        time.sleep(1)
    f.close()

save_source_urls()
