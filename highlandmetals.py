import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import json

class highlandmetals:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        navbarlist = []

        


    def getUrlofpage(self):
        self.driver.get(self.url)
        print("first function done")
    
    
    def getpageUrl(self):
        self.getUrlofpage()
        navbarlist = []
        hrefproduct = []
        navbar = driver.find_elements("xpath", '//a[@class = "dropdown-toggle"]')
        getproductatag = driver.find_elements(By.CSS_SELECTOR , "ul.navbar-nav>li a")
        for hrefnav in navbar:
            print(hrefnav.text)
            hrefnavs= hrefnav.get_attribute('href')
            navbarlist.append(hrefnavs)
        
        for a in getproductatag:
            href = a.get_attribute('href')
            hrefproduct.append(href)
        return hrefproduct

    def producturl(self):
        hrefproduct = self.getpageUrl()
        allproductcard =[]
        for lin in hrefproduct:
            driver.get(lin)
            print(lin)
            try:
                prodprod = driver.find_elements(By.CSS_SELECTOR, 'h2.xs-only-margin-top >a')
                for prods in prodprod: 
                    prods = prods.get_attribute('href')
                    allproductcard.append(prods)
            except:
                    print("page have no url --error")
        return allproductcard  
        
                  
    def tabledatap1(self):
        allproductcard = self.producturl()
        tabledata = []
        tableshrefs = []
        tableids = []
        tableimages = []
        qtyproduct = []
        qtys = []
        package =[]
        empty = []
        name = []
        for lins in allproductcard:
            driver.get(lins)
            print(lins)
            
            tablelist = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr>td>a.marginright')
            idlist = driver.find_elements(By.CSS_SELECTOR, 'tbody >tr>td>span')
            for tablist in tablelist:
                tabletexts = tablist.text
                tabledata.append(tabletexts)  
                tablehref = tablist.get_attribute('href')
                tableshrefs.append(tablehref)
                image = tablist.get_attribute('rel')
                tableimages.append(image)
                empty.append("")
                name.append("highlandmetals")
            for ids in idlist: 
                idno = ids.text
                tableids.append(idno)
            print(tabledata)
            print(tableshrefs)
            print(tableids) 
        
        for qty in tabledata:
            pattern = '(\.*\d{2,3})[\s/]*([A-Za-z]+)'
            matches = re.findall(pattern, qty)
            qtys.append(matches)
        for k in qtys:
            try:
                onlyqtys = k[1][0]
                print(onlyqtys)
                onlypack = k[1][1]
                print(onlypack)
            except:
                onlyqtys = "none"
                onlypack = 'none'
            qtyproduct.append(onlyqtys)
            package.append(onlypack) 
        print("good ho gaya")
        print(len(name))
        print(len(tableids))
        print(len(empty))
        print(len(tabledata))
        print(len(package))
        print(len(tableshrefs))
        print(len(tableimages))

        technologies= {
            "Seller Platform": name,
            "Seller SKU" : tableids,
            "Manufacturer Name":name,
            'Manufacturr Code':tableids,
            'Product Title':tabledata,
            'Description' : empty,
            "Packaging":package,
            'QTY':qtyproduct,
            "Catagory" : empty, 
            "Subcategory" : empty,
            "Product Page URL" : tableshrefs, 
            "Attachment URL" : empty,
            "Images URL" : tableimages
            }
        df = pd.DataFrame(technologies)
        df.to_csv("highlandmetals.xlsx",index=False)
     



if __name__ == "__main__":
    SPlatfrom = "Glo Science Solutions"
    url = "https://www.highlandmetals.com/store/main.aspx"
    driver = webdriver.Chrome()
    scraper = highlandmetals(driver,url)
    scraped = scraper.tabledatap1()
    time.sleep(5)