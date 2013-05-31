# -*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import cookielib, urllib2, re, MySQLdb

__author__ = 'Sebastian'

class GooglePoz():
    u"Klasa pozwalaj¹ca sprawdzaæ pozycjê danej strony w google"

    page            = 0
    page_code       = None
    key_word        = 'minecraft download'
    key_word = re.sub(' ', '+', key_word)
    standard_page   = str('https://www.google.pl/search?newwindow=1&q='+key_word+'&oq='+key_word)
    site            = standard_page
    search_page     = 'patrz.pl'
    position        = 0
    pagination      = ''
    i_p             = 1 #Incrementing position (Position number in google result)
    i_pa            = 1 #Incrementing page  (Page bumber where te page is finded in google result)
    # MySQL Connect
    host            = 'localhost'
    user            = 'root'
    password        = ''
    database        = 'google'
    def __init__(self):
        print('Inicjalizacja klasy')
       # if (self.site == self.standard_page):
       #     self.connect()
    def dbConnect(self):
        conn    =   MySQLdb.connect(self.host, self.user, self.password, self.database, use_unicode=1)
    def connect(self):
        if (self.site != False):
            cj      =   cookielib.CookieJar()
            opener  =   urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent,}
            request =   urllib2.Request(self.site, None, headers)
            try:
                response=   opener.open(request)
                if (response):
                    pass
            except TypeError:
                print('Nieudane po³¹czenie ' + str(TypeError.message))
            sp    = BeautifulSoup(response.read())
            self.page_code = sp
        else:
            print('Nie podano strony z któr¹ nale¿y siê po³aczyæ')


    def get_poz(self, key_word, search_page):
        key_word = re.sub(' ', '+', key_word)
        self.search_page        = search_page
        self.key_word           = key_word
        while (self.position == 0):
            if (self.page != 0):
                self.pagination = '&start='+str(self.page);
            self.site               = str('https://www.google.pl/search?newwindow=1&q='+self.key_word+'&oq='+self.key_word+self.pagination)
            self.connect()
            results = self.page_code.find(id="search")
            inside_ol = results.ol
            lis = inside_ol.findAll('li')
            for li in lis:
                if (li.a['href'].find(self.search_page) == -1):
                    pass
                elif(li.a['href'].find(self.search_page) != -1):
                    self.position = self.i_p

                print(str(self.i_p)+' '+str(li.a['href'].find(self.search_page)))
                self.i_p = self.i_p +1
            self.page   = int(self.page) + 10
            self.i_pa = self.i_pa + 1

if __name__=='__main__':
    #try:
    GooglePoz= GooglePoz()
    GooglePoz.get_poz('hosting www', 'prv.pl')
    print(GooglePoz.position)
    print(GooglePoz.page)
    #except TypeError:
        #print(TypeError.message)