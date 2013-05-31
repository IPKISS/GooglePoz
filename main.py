# -*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    #TODO: Add if possible small library that will be faken BeautifulSoup
import cookielib, urllib2, re, MySQLdb

__author__ = 'Sebastian'

class GooglePoz():
    u"This class allow you to check current position of your page in google result, for specified phrase"

    page            = 0
    page_code       = None
    key_word        = 'jakis artykul' #default keyword to search
    key_word        = re.sub(' ', '+', key_word)
    standard_page   = str('https://www.google.pl/search?newwindow=1&q='+key_word+'&oq='+key_word)
    site            = standard_page
    search_page     = 'onet.pl' # default page to search
    position        = 0
    pagination      = ''
    i_p             = 1 #Incrementing position (Position number in google result) #TODO I should change name of this and next varible
    i_pa            = 1 #Incrementing page  (Page bumber where te page is finded in google result)
    # MySQL Connect data
    host            = '127.0.0.1'
    user            = 'root'
    password        = ''
    database        = 'google'
    conn            = False
    def __init__(self):
        print('Class init')
       # if (self.site == self.standard_page):
       #     self.connect()
    def dbConnect(self):
        self.conn    =   MySQLdb.connect(self.host, self.user, self.password, self.database, use_unicode=1)
        return  self.conn

    def add_result(self, query):
        c   = self.conn.cursor()
        c.execute(query)
        self.conn.commit()

    def get_page(self, page_id):
        c   = self.conn.cursor()
        c.execute("SELECT * FROM pages WHERE id=%s", (page_id))
        for id, page in c.fetchall():
            return page
    def get_keyword(self, page_id):
        c   = self.conn.cursor()
        c.execute("SELECT * FROM keywords WHERE page_id=%s", (page_id))
        return c.fetchall()
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
                print('Nieudane połączenie ' + str(TypeError.message))
            sp    = BeautifulSoup(response.read())
            self.page_code = sp
        else:
            print('Nie podano strony z którą należy się połączyć')


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
                    #print self.i_p

                #print(str(self.i_p)+' '+str(li.a['href'].find(self.search_page)))
                self.i_p = self.i_p +1
            self.page   = int(self.page) + 10
            self.i_pa = self.i_pa + 1


    def reset_connection(self):
        self.i_p            = 1
        self.i_pa           = 1
        self.pagination     = ''
        self.position       = 0
        self.page_code      = None
        self.page           = 0
        self.site           = self.standard_page
if __name__=='__main__':
    #TODO: Add arguments that will allow run this script with paramer. Forexample main.py -s site_id  (Where site id is a number from database)
    #try:
    GooglePoz= GooglePoz()
    GooglePoz.dbConnect()
    #result = GooglePoz.get("SELECT * FROM result")
    #print(result)
    #GooglePoz.get_poz('hosting www', 'prv.pl')

    page        = GooglePoz.get_page('2')
    for id, page_id, keyword in GooglePoz.get_keyword('2'):
        print u'Pobieranie pozycja dla strony ' + page + u' - Słowa kluczowe ' + keyword
        GooglePoz.get_poz(keyword, page)
        print str(GooglePoz.position) +  ' ' + str(GooglePoz.page)
        GooglePoz.reset_connection() # This will allow newt iteration from begining

    #print(GooglePoz.position)
    #print(GooglePoz.page)
    #except TypeError:
        #print(TypeError.message)