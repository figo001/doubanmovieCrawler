#coding:utf-8
import urllib2
import cookielib
import time

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        send_headers = {'Host': 'movie.douban.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        req = urllib2.Request(url, headers = send_headers)
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read().encode('utf-8')
        time.sleep(3)
