

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import math

class facebook:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.list1 = []  
        self.list2 = [] 
        driver = webdriver.Chrome()
    
    def activedriver(self): 
        self.driver.get(self.url)
        time.sleep(1)
        try:
            cookie = {'name': 'c_user', 'value': '100088370955185'}
            self.driver.add_cookie(cookie)
            cookie = {'name': 'xs', 'value': '11%3An_o-KW90Tp57yw%3A2%3A1688979028%3A-1%3A-1'}
            self.driver.add_cookie(cookie)
            # refresh the page to apply the cookie
            self.driver.maximize_window()
            self.driver.refresh()
            time.sleep(1) 
           
        except:
            usernamedata = "atif123@codeaza-apps.com"
            passworddata = "Codeaza@Prod1234"
            username = driver.find_element("xpath", '//input[@name="email"]')
            password = driver.find_element("xpath", '//input[@name="pass"]')
            username.send_keys(usernamedata)
            password.send_keys(passworddata)
            time.sleep(1)
            loginbutton = driver.find_element("xpath", '//button[@name="login"]')
            loginbutton.click()
            time.sleep(1)
            print("but in this case need phone number")
            
            
    
    def gethuzaifadata (self):
        self.activedriver()
        filename = 'book1.csv'
        j = 0
        with open(filename, 'r' , encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row
            for row in csvreader:
                print(row[0], "profileurl")
                j += 1
                print(j, "now row number")
                self.list1.append(row[0])
            print(len(self.list1))
            time.sleep(1)

    def loginAddress(self):
        self.gethuzaifadata ()
        # try:
        
        worksdata = [] 
        placedsdata = []
        contactsdata = [] 
        familysdata = []
        detialsdata = []
        eventsdata = []
        
        
        #LIKE DATA
        urldata = []
        likealldata = []
        count = 0
        NaNdata = "NaN"
        
        #place 
        hometown = []
        currenttown = []
        contact_info = []
        genderdata = []
        website_social = []
        relationdata = []
        family_data = []
        aboutsdata = []
        eventmain =[]
        pronun = []
        othername = []
        favour =[]
        workssdata = []
        universityssdata = []
        highdata = []
        workssdata1 = []
        universityssdata1 = []
        highdata1 = []
        allmusic = []
        allfilm = []
        alltv = []
        allbook = []
        allevent = []
        allqus = []
        NODATA = "NaN"
        urldata = []
        allsports = []
        count = 0
        allrev = []
        
          
        
        
        
        urldata = []
        count = 0
        for link in self.list1:
            count = count + 1
            print(count , "no of profile")
            
            time.sleep(1)
            driver.get(link)
            time.sleep(1)
            print("check here")
            time.sleep(1)
            
            #about data ----------------here break 
            time.sleep(1) 
            try:
                about = driver.find_element("xpath", '//span[text()="About"]')
                time.sleep(4)
                about.click()
            except:
                time.sleep(5)
                continue
            urldata.append(link)
            #scroll function
            time.sleep(2)
            scroll_value = "window.scrollBy(0, window.innerHeight * 0.25);"
            driver.execute_script(scroll_value)
            time.sleep(1)
            
            print("Scroll down complete")
            arraysport = False 
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                sportsdata = driver.find_element("xpath", '//span[text()="Sports"]')
                time.sleep(1)
                sportsdata.click()
                time.sleep(2)
                try:
                    nosportdata = driver.find_element("xpath", '//span[text()="No sports to show"]')
                    time.sleep(1)
                    print(nosportdata.text , "--------------sport")
                    if "No" in nosportdata.text:
                        allsports.append(NODATA)
                        arraysport =True
                except:
                    sportdataexist = []
                    yessportdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for sport in yessportdata:
                        print(sport.text ,"its sport data")
                        sportdataexist.append(sport.text)
                    dataexistsport = ' ,'.join(sportdataexist)
                    print(dataexistsport ,"Sportdata")
                    allsports.append(dataexistsport)
                    arraysport = True
            except:
                if arraysport is False:
                    allsports.append(NODATA)
                    print(allsports ,"ghdydkty")
            print(allsports ,"sport ----- data ")
            print(allsports)
            print("@@@@@@@@@@@@@@@@@@@  sport  @@@@@@@@@@@@@@@2")
                
                
                
            
            
            arraymusic = False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                musicdata = driver.find_element("xpath", '//span[text()="Music"]')
                time.sleep(1)
                musicdata.click()
                time.sleep(2)
                print("after click")
                try:
                    nomusicdata = driver.find_element("xpath", '//span[text() ="No artists to show"]')
                    time.sleep(1)
                    print("idf no data ")
                    print(nomusicdata.text , "musicdata       ------------ music")
                    allmusic.append(NODATA)
                    arraymusic = True
                except:
                    print("if data ")
                    musicdataexist = []
                    yesmusicdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for mus in yesmusicdata:
                        print(mus.text)
                        musicdataexist.append(mus.text)
                    dataexistmusic = ' ,'.join(musicdataexist)
                    print(dataexistmusic ,"musicdata")
                    allmusic.append(dataexistmusic)
            except:
                if arraymusic is False:
                    allmusic.append(NODATA)
            print(allmusic ,"here data ")
            print("@@@@@@@@@@@@@@@@@@@  MUSIC  @@@@@@@@@@@@@@@2")
                
                    
            
            
           
# #             ###################FILMS
            arrayfilm = False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                filmsdata = driver.find_element("xpath", '//span[text()="Films"]')
                time.sleep(1)
                filmsdata.click()
                #here films
                time.sleep(2)
                try:
                    nofilmdata = driver.find_element("xpath", '//span[text()="No films to show"]')
                    time.sleep(1)
                    print(nofilmdata.text , "films  ------------ film")
                    if 'No' in nofilmdata.text:
                        allfilm.append(NODATA)
                        arrayfilm = True  
                except:
                    filmdataexist = []
                    yesfilmdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for film in yesfilmdata:
                        print(film.text)
                        filmdataexist.append(film.text)
                    dataexistfilm = '  ,'.join(filmdataexist)
                    print(dataexistfilm ,"filmdata")
                    allfilm.append(dataexistfilm)
            except:
                print("film data if break")
                if arrayfilm is False:
                    allfilm.append(NODATA)
                
            print(allfilm)
            print("@@@@@@@@@@@@@@@@@@@ films @@@@@@@@@@@@@@@2")
            
            
            arraytv = False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)  
                print("here ")              
                tvdata = driver.find_element("xpath", '//span[contains(., "TV")]')
                time.sleep(1)
                tvdata.click()
                time.sleep(2)
                try:
                    try:
                        notvdata = driver.find_element("xpath", '//span[text() = "No Watched to show"]')
                        time.sleep(1)
                        print(notvdata.text , "-------------- tvdata")
                        if 'No' in notvdata.text:
                            alltv.append(NODATA)
                            arraytv =True
                    
                    except:
                        notvdata = driver.find_element("xpath", '//span[text() = "No TV Programmes to show"]')
                        time.sleep(1)
                        print(notvdata.text , "-------------- tvdata")
                        if 'No' in notvdata.text:
                            alltv.append(NODATA)
                            arraytv = True   
                except:
                    tvdataexist = []
                    yestvdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for tv in yestvdata:
                        print(tv.text)
                        tvdataexist.append(tv.text)
                    dataexisttv = '  ,'.join(tvdataexist)
                    alltv.append(dataexisttv)
            except:
                print("musicdata empty")
                if arraytv is False:
                    alltv.append(NODATA)
            print(alltv)
            print("@@@@@@@@@@@@@@@@@@@   TV PROGRAMMES  @@@@@@@@@@@@@@@2")
           
           
           ##################here books okay
            arraybook =False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                bookdata = driver.find_element("xpath", '//span[text()="Books"]')
                time.sleep(1)
                bookdata.click()
                time.sleep(2)
                #here films
                try:
                    nobookdata = driver.find_element("xpath", '//span[text()="No books to show"]')
                    time.sleep(1)
                    print(nobookdata)
                    if 'No' in nobookdata.text:
                        allbook.append(NODATA) 
                        arraybook =True
                except:
                    bookdataexist = []
                    yesbookdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for book in yesbookdata:
                        print(book.text ,"book data heree")
                        bookdataexist.append(book.text)
                    dataexistbook = '  ,'.join(bookdataexist)
                    allbook.append(dataexistbook)
                    print(allbook ,"all book ")
            except:
                print("musicdata empty")
                if arraybook is False:
                    allbook.append(NODATA)
            print(allbook)
            print("@@@@@@@@@@@@@@@@@@@ BOOKs @@@@@@@@@@@@@@@2")
            
            
            
            
            ##################here books okay
            arrayevent = False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                eventdata = driver.find_element("xpath", '//span[text()="Events"]')
                time.sleep(1)
                eventdata.click()
                time.sleep(2)
                #here films
                try:
                    noeventdata = driver.find_element("xpath", '//span[text() = "No events to show"]') 
                    time.sleep(1)
                    print(noeventdata.text , "----------------event data")
                    if 'No' in noeventdata.text:
                        allevent.append(NODATA)
                        arrayevent = True
                except:
                    eventdataexist = []
                    yeseventdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for event in yeseventdata:
                        print(event.text , "event data is here ")
                        eventdataexist.append(event.text)
                    dataexistevent = ' ,'.join(eventdataexist)
                    allevent.append(dataexistevent)
            except:
                print("musicdata empty")
                if arrayevent is False:
                    allevent.append(NODATA)
            print(allevent)
            print("@@@@@@@@@@@@@@@@@@@ event @@@@@@@@@@@@@@@2")
            
            
            
            
            
            
            
            
#              ##################here books okay
            arrayqus =  False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                qusdata = driver.find_element("xpath", '//span[text()="Questions"]')
                time.sleep(1)
                qusdata.click()
                #here films
                try:             
                    noqusdata = driver.find_element("xpath", '//span[text()="No activity to show"]')
                    time.sleep(1)
                    print(noqusdata.text , "-------------------no ques data")
                    if 'No' in noqusdata.text:
                        allqus.append(NODATA)
                        arrayqus = True
                except:
                    qusdataexist = []
                    yesqusdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for qus in yesqusdata:
                        # print(qus.text , "event data is here ")
                        qusdataexist.append(qus.text)
                    dataexistqus = ', '.join(qusdataexist)
                    allqus.append(dataexistqus)
            except:
                print("musicdata empty")
                if arrayqus is False:
                    allqus.append(NODATA)
                print(allqus)
            print("@@@@@@@@@@@@@@@@@@@  question  @@@@@@@@@@@@@@@@@@")
            
            
            
            
            
             ################## reviews
            arrayrev = False
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
                time.sleep(1)                
                revdata = driver.find_element("xpath", '//span[text()="Reviews given"]')
                time.sleep(1)
                revdata.click()
                #here films
                try:
                    norevdata = driver.find_element("xpath", '//span[text() = "No activity to show"]')
                    time.sleep(1)
                    print(norevdata.text ,"--------------------- no res data")
                    if 'No' in norevdata.text:
                        allrev.append(NODATA)
                        arrayrev = False
                except:
                    revdataexist = []
                    yesrevdata = driver.find_elements("xpath", '//div[@class="x1iyjqo2 x1pi30zi"]//span')
                    time.sleep(1)
                    for rev in yesrevdata:
                        print(rev.text , "event data is here ")
                        revdataexist.append(rev.text)
                    dataexistrev = ', '.join(revdataexist)
                    allrev.append(dataexistrev)
                
            except:
                print("musicdata empty")
                if arrayrev is False:
                    allrev.append(NODATA)
            print(allrev)
            print("@@@@@@@@@@@@@@@@@@@   review given @@@@@@@@@@@@@@@@@@")
                        
                    
            
                    
                    
            
            
            #about data ---------------- here we add data of like
            time.sleep(1) 
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
            except:
                time.sleep(5)
                continue
           
           
          
                
        #event 
       
        print(len(allmusic))
        print(len(allfilm))
        print(len(alltv))
        print(len(allbook))
        print(len(allevent))
        print(len(allqus))
        print(len(allrev))
        technologies= {
            
            "URl":urldata,
            "Music":allmusic,
            "Films":allfilm,
            "TV":alltv,
            "Book":allbook,
            "Event":allevent,
            "Question":allqus,
            "Review Given":allrev
            
            }
        
        df = pd.DataFrame(technologies)
        df.to_csv("samplemaindata201t400-100088291850242.csv",index=False)
        return df
          
          
          
          
          
          
          
                
        # except:
        #     print("for private account")

                
                
                    

if __name__ == "__main__":
   
    url = "https://www.facebook.com/"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    scraper = facebook(driver,url)
    driver.implicitly_wait(3)
    scraped = scraper.loginAddress()       