import cPickle
import sys
def find_urls(keyword,index):
	if keyword in index:
		return index[keyword]
	else:
		return

def find_all(keywords, index):
	urls = []
	for keyword in keywords:
		new_urls=find_urls(keyword,index)
		urls = list(set(urls) | set(new_urls))
	return urls

if __name__ == "__main__":
	index = cPickle.load(open(sys.argv[1]))
	urls = find_all(sys.argv[2:],index)
	for url in urls:
		print url
