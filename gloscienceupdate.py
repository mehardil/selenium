import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

class gloscience:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.Description = []


    def getUrlofpage(self):
        self.driver.get(self.url)
        print("first function done")
    
    
    def getpageUrl(self):
        self.getUrlofpage()
        pagehref = []
        pageurl = []
        shop = driver.find_element("xpath","//li[@class ='site-nav__item site-nav__expanded-item site-nav--has-dropdown site-nav--active']")
        ultags = shop.find_element(By.TAG_NAME, 'ul')
        list_links=ultags.find_elements(By.TAG_NAME, 'li')
        for e1 in list_links:
            ppp = e1.find_element(By.TAG_NAME, 'a')
            pagehref.append(ppp.get_attribute('href'))
        for j in pagehref:
            driver.get(j)
            producturls  = driver.find_elements(By.CLASS_NAME , "grid-product__link")
            for t1 in producturls:
                pageurl.append(t1.get_attribute('href'))
        print("second function done")
        return pageurl

       


    def getproductdata(self):
        pageurl = self.getpageUrl()
        qtysproduct = []
        respon = []           
        for k in pageurl:
            driver.get(k)
            print(k)
            qty =  driver.find_element(By.XPATH, "//input[@name = 'quantity']" )
            skuscript = driver.find_element(By.XPATH, "//script[@type = 'application/ld+json']" )
            skudata = skuscript.get_attribute('innerHTML')
            qtys = qty.get_attribute('value')
            qtysproduct.append(qtys)
            print(skuscript.text)
            res2 = json.loads(skudata)
            respon.append(res2) 
        
        print("three function complete")   
        return respon,qtysproduct      

    
    def resp(self):
        respon , qtysproduct = self.getproductdata()
        
        skundescriptions1 = []
        skunamedata = []
        skuimage = []
        skuurl = []
        skudata =[]
        skuwebname =[]
        skucolempty = []
       

        for i in respon:

            webname = "gloscience"
            skuwebname.append(webname)
            colempty = " "
            skucolempty.append(colempty)
              
                       
            names = i["name"]
            skunamedata.append(names)
        
            description = i["description"]
            skundescriptions1.append(description)
    
            images = i["image"]["image"]
            skuimage.append(images)
    
            skudat = i["offers"][0]["sku"]
            skudata.append(skudat)
    
            url = i["offers"][0]["url"]
            skuurl.append(url)




        technologies= {
            "Seller Platform": skuwebname,
            "Seller SKU" : skudata,
            "Manufacturer Name":skuwebname,
            'Manufacturer Code':skudata,
            'Product Title':skunamedata,
            'Description' : skundescriptions1,
            "Packaging":skucolempty,
            'QTY':qtysproduct,
            "Catagory" : skucolempty, 
            "Subcategory" : skucolempty,
            "Product Page URL" : skuurl, 
            "Attachment URL" : skucolempty,
            "IImages URL" : skuimage
    
            }
        df = pd.DataFrame(technologies)
        df.to_csv("sellerPlatform.csv",index=False)
        return df


if __name__ == "__main__":
    SPlatfrom = "Glo Science Solutions"
    url = "https://gloscience.com/collections/all-glo-products"
    driver = webdriver.Chrome()
    scraper = gloscience(driver,url)
    scraped = scraper.resp()
    time.sleep(5)

