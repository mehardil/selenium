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
        self.ProductPageUrl = []
        self.ProductNames = []
        self.Catagory = []
        self.sku = []
        self.SubCatagory = []
        self.Qty = []
        self.ManufacturerName = []
        self.ManufacturerCode = []
        self.SellerPlatform = []
        self.Packaging = []
        self.AttchmentUrl = []
        self.Pagehref = []
        self.hreftext = []
        self.producturl = []
        self.test = []
        self.respon = []
        self.qtysproduct =[]
        self.skundescriptions1 = []
        self.skunamedata = []
        self.skuimage = []
        self.skuurl = []
        self.skudata =[]
        self.skuurl1 = []
        self.skudata1 =[]
        self.list_link = []
                
    def getUrl(self):
        self.driver.get(self.url)
    
    def getCategoryUrl(self):
        self.getUrl()
        pagehref = []
        test = []
        shop = driver.find_element("xpath","//li[@class ='site-nav__item site-nav__expanded-item site-nav--has-dropdown site-nav--active']")
        ultags = shop.find_element(By.TAG_NAME, 'ul')
        print(ultags.get_attribute('class'))
        list_links=ultags.find_elements(By.TAG_NAME, 'li')
        for e1 in list_links:
            ppp = e1.find_element(By.TAG_NAME, 'a')
            pagehref.append(ppp.get_attribute('href'))
            print(ppp.get_attribute('href'))

        print(pagehref)
        for j in pagehref:
            driver.get(j)
            producturls  = driver.find_elements(By.CLASS_NAME , "grid-product__link")
            for t1 in producturls:
                test.append(t1.get_attribute('href'))
        print(test)
        return test

       


    def qtysprod(self):
        test = self.getCategoryUrl()
        qtysproduct = []
        respon = []           
        for k in test:
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
        print(respon)    
        return respon       

    
    def resp(self):
        respon = self.qtysprod()
        skundescriptions1 = []
        skunamedata = []
        skuimage = []
        skuurl = []
        skudata =[]
        skuurl1 = []
        skudata1 =[] 

        for i in respon:
                       
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

            'Seller SKU ': skudata ,
            'Manufacturer Code ':skudata,
            'Product Title':skunamedata,
            'Description' : skundescriptions1,
            # 'QTY':qtysproduct,
            'Attachment URL':skuurl,
            'Images URL':skuimage,
    
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

