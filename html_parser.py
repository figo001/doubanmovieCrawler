#coding:utf-8
import re
import sys
import urlparse
import pdb
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')




class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r'https\:\/\/m.+?page'))
        # print links
        # pdb.set_trace()
        for link in links:
            new_url = link['href']
            new_full_url = new_url
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        return res_data

