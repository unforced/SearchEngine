import web_crawler
import re
import sys
import cPickle
def get_keywords(url):
	contents = web_crawler.get_page(url)
	words = re.split('\W+',contents)
	return words

def create_index():
	return {}

def add_to_index(url,index):
	words = get_keywords(url)
	for word in words:
		if word in index:
			if url not in index[word]:
				index[word].append(url)
		else:
			index[word] = [url]

def add_all_to_index(urls,index):
	for url in urls:
		add_to_index(url,index)

def build_index(urls):
	index = create_index()
	add_all_to_index(urls,index)
	return index

def crawl_build(seed,depth):
	urls = web_crawler.crawl_web(seed,depth)
	return build_index(urls)

def crawl_add(seed,depth,index):
    urls = web_crawler.crawl_web(seed,depth)
    add_all_to_index(urls,index)

if __name__ == "__main__":
	f = open(sys.argv[3], 'r')
	i = {}
	try:
		i = cPickle.load(f)
	except:
		i = {}
	f.close()
	crawl_add(sys.argv[1], int(sys.argv[2]), i)
	f = open(sys.argv[3], 'w')
	cPickle.dump(i, f)


