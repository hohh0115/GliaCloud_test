# -*- coding: utf-8 -*-

from collections import Counter

def counting(urls_list, top_count=3):

	file_names = []
	for url in urls_list:
		file_names.append(url.split('/')[-1])

	top_count_file_names = Counter(file_names).most_common(top_count)
	for i in top_count_file_names:
		print(i[0], i[1])

if __name__ == '__main__':

	urls = [
		"http://www.google.com/a.txt",
		"http://www.google.com.tw/a.txt",
		"http://www.google.com/download/c.jpg",
		"http://www.google.co.jp/a.txt",
		"http://www.google.com/b.txt",
		"https://facebook.com/movie/b.txt",
		"http://yahoo.com/123/000/c.jpg",
		"http://gliacloud.com/haha.png",
	]

	counting(urls)