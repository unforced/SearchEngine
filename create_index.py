import web_crawler
import re
import sys
import pickle
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

if __name__ == "__main__":
	i = crawl_build(sys.argv[1], int(sys.argv[2]))
	if len(sys.argv)>3:
		f = open(sys.argv[3], 'w')
		pickle.dump(i, f)
	else:
		print i
