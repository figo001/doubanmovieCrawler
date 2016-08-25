#-*- coding:utf-8 -*-

import sys
import html_downloader
import html_outputer
import html_parser
import url_manager
import pdb
import urllib2
import re
import json
import time

reload(sys)
sys.setdefaultencoding('utf8')

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        # pdb.set_trace()
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawl %d:%s' % (count, new_url)
                # pdb.set_trace()
                time.sleep(1)
                html_cont = self.downloader.download(new_url)
                # print html_cont
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if 1000 == count:
                    break
                count += 1
            except:
                print 'crawl failed'

        fp1 = open('111.txt','w')
        fp2 = open('result.txt', 'w')
        fp2.write('名称\t\t评分\t\t人数\n')
        term_urls = self.urls.get_old_urls()
        num = 1

        for url in term_urls:
            # pdb.set_trace()
            try:
                id = re.search(r'\d+', url).group()
                full_url = 'https://api.douban.com/v2/movie/subject/' + str(id)
                fp1.write(url)
                fp1.write('\n')
                id = re.search(r'\d+',url).group()
                full_url = 'https://api.douban.com/v2/movie/subject/' + str(id)
                response = urllib2.urlopen(full_url)
                cont = response.read()
                s = json.loads(cont, encoding='utf-8', strict=False)
                tset = s['title']
                print num, s['title'], s['rating']['average'], s['ratings_count'],
                print full_url
                fp2.write(s['title'])
                fp2.write('\t\t\t\t')
                fp2.write(str(s['rating']['average']))
                fp2.write('\t\t\t\t')
                fp2.write(str(s['ratings_count']))
                fp2.write('\n')
                num += 1
                time.sleep(1)
            except:
                continue

        fp1.close()
        fp2.close()



if __name__=="__main__":
    root_url = 'https://movie.douban.com/subject/25966028/'
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)