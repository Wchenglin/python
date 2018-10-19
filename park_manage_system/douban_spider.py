from urllib import request
import re

class Douban_Spider(object):
    url = 'https://book.douban.com/top250?start='
    root_pattern = '<td valign="top">([\s\S]*?)</td>'
    # book_name_pattern = 'title="(.*?)"[\s\S]*?'
    # book_details_pattern = '<p class="pl">([\s\S]*?)</p>'
    # intro_pattern = '<span class="inq">([\s\S]*?)</span>'
    url_pattern = '<a href="(.*?)"[\s\S]*?'

    def __list(self):
        list_url = [0,25,50,75,100,125,150,175,200,225]
        url_anchors = []
        for _url in list_url:
            url = 'https://book.douban.com/top250?start='+str(_url)
            url_anchors.append(url)
        return url_anchors

    def __fetch_content(self,url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls,encoding = 'utf-8')
        return htmls
        
    def __analysis(self,htmls):
        root_htmls = re.findall(Douban_Spider.root_pattern,htmls)
        list1 = []
        for html in root_htmls:
            # book_name = re.findall(Douban_Spider.book_name_pattern,html)
            # book_details = re.findall(Douban_Spider.book_details_pattern,html)
            # intro = re.findall(Douban_Spider.intro_pattern,html)
            book_url = re.findall(Douban_Spider.url_pattern,html)
            # print(str(book_url)+' '+str(book_name)+' '+str(book_details)+' '+str(intro))
            list1.append(book_url)
        return list1
        
    def go(self):
        lsit2 = []
        url_anchors = self.__list()
        for url in url_anchors: 
            htmls = self.__fetch_content(url)
            lsit2.append(self.__analysis(htmls))
        return lsit2

class BookDetails(Douban_Spider):
    root_pattern = '<div id="info" class="">([\s\S]*?)</div>'
    book_pattern = '>([\s\S]*?)<'

    def __get_url(self):
        url = super(BookDetails,self).go()[0][0][0]
        return url

    def __fetch_content(self,url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls,encoding = 'utf-8')
        return htmls

    def __analysis(self,htmls):
        htmls = re.findall(BookDetails.root_pattern,htmls)
        books = re.findall(BookDetails.book_pattern,htmls)
        print(books)

    def go(self):
        url = self.__get_url()
        htmls = self.__fetch_content(url)
        self.__analysis(htmls)
        

bookdetails = BookDetails()
bookdetails.go()


