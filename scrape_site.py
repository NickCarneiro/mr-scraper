import thread
import threading
from datetime import datetime
from username_store import Username_Store

def main():
    f = open('source_urls.data')
    urls = f.readlines()
    f.close()
    #construct list of dicts with urls and domains
    sources = []
    for url in urls:
        domain = url.replace('http://', '').split('/')[0]
        sources.append({'url': url, 'domain': domain})
    output_file = str(now.year()) + '_' + str(now.month()) + '_' +str(now.day) + '_' + str(now.hour) + \
                  str(now.minute) + '.data'
    now = datetime.now()
    print 'initializing username store with output file', output_file
    username_store = Username_Store(output_file)
    #spin up 10 threads at a time to work on these urls
    max_threads = 10
    for i in range(0, max_threads):
        print 'spinning up thread', str(i)


#we have list of 100 possible sources. try and scrape 10k users from them all asynchronously
"""
returns a username from a user page like this: http://www.way2hope.org/family-forums/index.php?s=449af9ac4cfb4fd398cdbf738bdea29f&showuser=56949
returns false if something goes wrong
"""
def extract_username(url):
    return False

"""
sequentially scrape all usernames from a forum at @url
"""
def scrape_source(url, domain, username_store):
    #just try to scrape the first 10k
    username_count_guess = 10000
    page_index = url.find('index.php')
    #some urls have index.php?asdf=blah in them. cut this off so they all look like blah.com/forum/
    if page_index != -1:
        #truncate
        url = url[0:page_index]
    url_stub = url + 'index.php?showuser='
    #now we can just tack ints on to the end of this string to get usernames
    error_count = 0
    # give up on this url once we reach this many errors
    error_threshold = 10
    for i in range(0, username_count_guess):
        if error_count >= error_threshold:
            print 'Hit the error threshold on %s' % domain
        username = extract_username(url_stub + str(i))
        if username == False:
            error_count += 1
            print 'Could not get username number %d. Have encountered %d errors on url stub %s' % (i, errors_count, url_stub)
        else:
            username_store.store_username(username, domain)
main()