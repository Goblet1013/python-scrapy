# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from pro_spider.items import ProSpiderItem
class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=山东科技大学&pn=0']
    first_url='http://tieba.baidu.com/f?kw=山东科技大学&pn='
    page_num = 0
    def parse(self, response):
        #print(response.text)
        soup=BeautifulSoup(response.text,'html.parser')
        tiezi=soup.find_all('li',class_=' j_thread_list clearfix')
        print(len(tiezi))
        item = ProSpiderItem()
        for i in tiezi:
            try:
                item['authors'] = i.find('span',class_='tb_icon_author ')['title']
                print(item['authors'])
                item['text'] = i.find('div', class_='threadlist_abs threadlist_abs_onlyline ').string.strip()
                print(item['text'])
                item['reply_nums'] = i.find('span',class_='threadlist_rep_num center_text').string
                print(item['reply_nums'])
                print('================================================')
                yield item
            except:
                continue
        if self.page_num<1000:#470500
            self.page_num+=1
            print('爬取第%d页' % (self.page_num))
            page_url=self.first_url+str(self.page_num*50)
            print(page_url)
            #callback回调函数，解析页面
            yield scrapy.Request(url=page_url,callback=self.parse)