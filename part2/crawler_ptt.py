
import requests
from bs4 import BeautifulSoup
import sys

class Crawler_PTT:

	def __init__(self, board_name):
		self.board_name = board_name
		self.base_url = 'https://www.ptt.cc'

	def get_soup_object(self, url):
		req = requests.get(url, cookies={"over18":"1"})
		return BeautifulSoup(req.text, 'html.parser')  # get BeautifulSoup object

	def get_to_work(self):
		self.board_url = "https://www.ptt.cc/bbs/{board_name}/index.html".format(board_name=self.board_name)
		soup = self.get_soup_object(self.board_url)

		for thread in soup.find_all(class_='r-ent'):
			date = thread.find('div', attrs={'class': 'date'}).text
			author = thread.find('div', attrs={'class': 'author'}).text
			if thread.find('a'):
				title = thread.find('div', attrs={'class': 'title'}).text
				content_path = self.base_url + thread.find('a')['href']
				# get content of the thread
				soup = self.get_soup_object(content_path)
				content = soup.find("div", {"id":"main-container"}).text
			print("===========================")
			print("日期", date)
			print("作者", author)
			print("標題", title)
			print("內文", content)
			print("看板名稱", self.board_name)
			print("===========================")

if __name__ == '__main__':
	board_name = 'NBA'
	crawler = Crawler_PTT(board_name)
	crawler.get_to_work()