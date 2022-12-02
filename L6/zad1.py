from bs4 import BeautifulSoup
import requests
import re

def get_html(url):
    r = requests.get(url)
    return r.text


def crawl(url, max_depth, action):

    visited_urls = set()
    result = []

    def scrape(url, depth, action): 
        if depth < 0 or url in visited_urls:
            return 
        
        # if unable to get contents of site, skip it
        try:
            content = get_html(url)
        except:
            return
        
        visited_urls.add(url)

        # perform operations on page's content
        result.append((url, action(content)))
        # recursively scrape sub_pages
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup.find_all('a', href = True):
            sub_url = tag.get('href')
            
            if sub_url.startswith('/'):
                sub_url = url+sub_url
            scrape(sub_url, depth-1, action)

    scrape(url, max_depth, action)
    return result

def remove_tags_from_text(text):
    text_tab = text.split()
    res = []
    for s in text_tab:
         if s == '':
             continue
         if s[0] != '<' or s[-1] == '<':
            res.append(s)
    return ' '.join(res)

def find_all_sentences(text, sentence):
    pattern = '[^.<>]* ' + sentence + ' [^.]*[\.<>]'
    res = re.findall(pattern, text)
    res = [remove_tags_from_text(x) for x in res]

    return res

if __name__ == "__main__":
    res = crawl("http://www.ii.uni.wroc.pl", 1, lambda x : "stypendia" in x)

    # does not really work that well, but gives some context
    # note: probably bad idea to parse html with regex 
    #res = crawl("http://www.ii.uni.wroc.pl", 1, lambda x : find_all_sentences(x, 'Python'))
    cnt = 0
    for  (url, act_result) in res:
        if act_result:
            print(f"{cnt}: {url} {act_result}")
            cnt+=1
    
