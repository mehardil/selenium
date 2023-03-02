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
        prodcolor = []
        prodimg = []          
        for k in pageurl:
            driver.get(k)
            print(k)
            qty =  driver.find_element(By.XPATH, "//input[@name = 'quantity']" )
            skuscript = driver.find_element(By.XPATH, "//script[@type = 'application/ld+json']" )
            skudata = skuscript.get_attribute('innerHTML')
            qtys = qty.get_attribute('value')

            temp = []
            color =  driver.find_elements(By.CSS_SELECTOR , "label.color-swatch")
            for t1 in color:
                temp.append(t1.text)
                st = ""
                for ee in temp:
                    st += ee
            prodcolor.append(st)
            temp1 = []
            com =  driver.find_elements(By.CSS_SELECTOR , "a.image-wrap")
            for t2 in com:
                temp1.append(t2.get_attribute('href'))
                st1 = ""
                for ee1 in temp1:
                    st1 += ee1
            prodimg.append(st1)



            qtysproduct.append(qtys)
            print(skuscript.text)
            res2 = json.loads(skudata)
            respon.append(res2) 
        
        print("three function complete")
        print(prodimg)  
        print("@@@@@@@@@2")

        print("three function complete   color")
        print(prodcolor)  
        print("#############")  
        return respon,qtysproduct ,prodcolor ,prodimg       

    
    def resp(self):
        respon , qtysproduct ,prodcolor ,prodimg = self.getproductdata()
        
        skundescriptions1 = []
        skunamedata = []
        skuimage = []
        skuurl = []
        skudata =[]
        skuwebname =[]
        skucolempty = []
        skufullname = []
       

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


        
            # for w in range(0,len(skunamedata)):
            #     fullname = skunamedata[w] + " ---- " +prodcolor[w]
            #     skufullname.append(fullname)



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
            "Images URL" : prodimg
    
            }
        df = pd.DataFrame(technologies)
        df.to_csv("gloscience.csv",index=False)
        return df


if __name__ == "__main__":
    SPlatfrom = "Glo Science Solutions"
    url = "https://gloscience.com/collections/all-glo-products"
    driver = webdriver.Chrome()
    scraper = gloscience(driver,url)
    scraped = scraper.resp()
    time.sleep(5)