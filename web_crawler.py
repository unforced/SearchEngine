import urllib
import sys
def get_page(link):
    page = ' '
    try:
	    page = urllib.urlopen(link).read()
    except IOError:
        page = ' '
    return page

def union(p, q):
	for e in q:
		if e not in p:
			p.append(e)

def get_next_target(page):
	start_link = page.find('a href=')
	if start_link==-1:
		return None,0
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

def get_all_links(page,depth):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append([url,depth-1])
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed,max_depth):
	tocrawl=[[seed,max_depth]]
	crawled=[]
	while tocrawl:
		page = tocrawl.pop()
		if page[0] not in crawled and page[1]>=0:
			union(tocrawl, get_all_links(get_page(page[0]),page[1]))
			crawled.append(page[0])
	return crawled

if __name__=="__main__":
    print crawl_web(sys.argv[1],int(sys.argv[2]))

