import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

class euobserver:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.alldata = []
        self.single_list = []
        self.highlightsdata = []
        self.authornamedata = []
        self.authorgmaildata = []
        self.authortwitterdata = []
        self.imagedata  = []
        self.timedata = []
        
    
    def getUrlofpage(self):
        self.driver.get(self.url)
        print("first function done")

    
    
    def getpageUrl(self):
        keywords = [ "Digital Market Act","Digital Services Act","Data Privacy","GDPR" ,"Cybsersecurity", "ePrivacy Regulation", "Copyright Directive", "Data Governance Act ", "The Cybersecurity Act"]
        for keyword in keywords:
            driver.execute_script("document.querySelector('body > header > div.my-nav.min-medium > ol.search.horizontal > li:nth-child(2) > form > input[type=text]').value = '';")
            driver.execute_script("document.querySelector('body > header > div.my-nav.min-medium > ol.search.horizontal > li:nth-child(2) > form > input[type=text]').value = '%s';"%keyword)
            driver.execute_script("document.querySelector('body > header > div.my-nav.min-medium > ol.search.horizontal > li:nth-child(1) > a').click()")
            hrefofallnews = driver.find_elements(By.CSS_SELECTOR, 'article.col-8 >div.grid>div.col-12>h5>a')
            gethrefs = []
            for link in hrefofallnews:
                href = link.get_attribute("href")
                gethrefs.append(href)
            self.alldata.append(gethrefs)
            while True:
                newpagedata = []
                try:
                    nextbutton = driver.find_element(By.CSS_SELECTOR, 'input[name = next]')
                    nextbutton.click()
                    newpagedata = driver.find_elements(By.CSS_SELECTOR, 'article.col-8 >div.grid>div.col-12>h5>a')
                    gethrefnext = []
                    for newdata in newpagedata:
                        href1 = newdata.get_attribute("href")
                        gethrefnext.append(href1)
                    self.alldata.append(gethrefnext)
                except:
                    break
        print("second function done")
        return self.alldata        
        
    def spliturl(self):
        for sub_list in self.alldata:
            for item in sub_list:
                self.single_list.append(item)
                print(item)
        print("third function done")        
        return self.single_list

    def getnewsdata(self):
        j =0
        for link in self.single_list:
            driver.get(link)
            print(link)
            j=j+1
            print(j)
            try:
                highlights = driver.find_element(By.CSS_SELECTOR, 'article.line-sep>h1')
                self.highlightsdata.append(highlights.text)
            except:
                self.highlightsdata.append("none")
        
            try:
                authorname = driver.find_element(By.CSS_SELECTOR, 'article.line-sep>p>span>a')
                self.authornamedata.append(authorname.text)
            except:
                self.authornamedata.append("none")
        
            try:
                authorgmail = driver.find_element("xpath", '//article/p/a[@data-icon="o"]')
                self.authorgmaildata.append(authorgmail.get_attribute('href'))
            except:
                self.authorgmaildata.append("none")
        
            try:
                authortwitter = driver.find_element("xpath", '//article/p/a[@data-icon="l"]')
                self.authortwitterdata.append(authortwitter.get_attribute('href'))
            except:
                self.authortwitterdata.append("none")
  
            try:
                image = driver.find_element(By.CSS_SELECTOR, 'article.line-sep>div.image-list>ul>li>figure>a>img')
                self.imagedata.append(image.get_attribute('src')) 
            except:
                self.imagedata.append("none")
    
            try:
                time = driver.find_element("xpath", '/html/body/main/div[1]/div[1]/div/article/time')
                self.timedata.append(time.text)
            except:
                self.timedata.append("none")
        print("forth done")

    def makedataframe(self):
        self.getUrlofpage()
        self.getpageUrl()
        self.spliturl()
        self.getnewsdata()
        technologies= {
        "News Highlights":self.highlightsdata,
        "Publisher Name" :self.authornamedata,
        "Publisher Gmail":self.authorgmaildata,
        'Publisher Twitter':self.authortwitterdata,
        'News URL':self.single_list,
        'Date':self.timedata,
        'News Image':self.imagedata
        }
        df = pd.DataFrame(technologies)
        df.to_csv("euobserver-newsdata.csv",index=False) 


    


    

if __name__ == "__main__":
   
    url = "https://euobserver.com/"
    driver = webdriver.Chrome()
    scraper = euobserver(driver,url)
    scraped = scraper.makedataframe()
    