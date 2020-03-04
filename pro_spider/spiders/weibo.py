# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from pro_spider.items import WeiboItem
import pymysql
class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com']
    first_url = 'https://s.weibo.com/weibo?q=山东科技大学&page='
    start_urls = ['https://s.weibo.com/weibo?q=山东科技大学&page=1']
    page_num = 1

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tiezi = soup.find_all('div', class_='card-wrap',attrs={'action-type':"feed_list_item"})
        print(len(tiezi))
        item = WeiboItem()#t=t.xpath('string(.)').extract()

        txts = response.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div/div[1]/div[2]/p[1]')
        flag=0
        for i in tiezi:
            try:
                #作者
                item['authors'] = i.find('a', class_='name').string
                print(item['authors'])
                #内容
                item['text'] = txts[flag].xpath('string(.)').extract()[0].strip()
                flag += 1
                print(item['text'])
                #转发量t=crad_wrap_list[0].xpath('string(.)').extract()
                a = i.find('div', class_='card-act').find('li').next_sibling.next_sibling
                if a.string.strip(' ')== '转发': a.string = '转发 0'
                else: a.string = a.string[1:]
                item['repost'] = a.string
                print(item['repost'])
                #评论数
                a = a.next_sibling.next_sibling
                if a.string.strip(' ') == '评论':a.string = '评论 0'
                item['comment_nums'] = a.string
                print(item['comment_nums'])
                #点赞数
                a = a.next_sibling.next_sibling.find('em').string
                if a == None : a = '点赞 0'
                else: a ='点赞 '+a
                item['praise'] = a
                print(item['praise'])
                print('================================================')
                yield item
            except:
                continue
        if self.page_num <= 47:
            self.page_num += 1
            #print('爬取第%d页' % (self.page_num))
            page_url = self.first_url + str(self.page_num)
            #print(page_url)
            # callback回调函数，解析页面
            yield scrapy.Request(url=page_url, callback=self.parse)

        # page_list=response.xpath('//*[@id="pl_feedlist_index"]/div[2]/div/a/@href').extract()
        # print(page_list)
        #
        #
        # #爬取多页信息
        # for page in page_list :
        #     from scrapy.http import Request
        #     page='https://s.weibo.com/'+page
        #     yield Request(url=page,callback=self.parse)
