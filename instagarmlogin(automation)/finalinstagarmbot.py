from selenium import webdriver
from selenium.webdriver.common.by import By
import json

class euobserver:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.list1 = []  
        self.list2 = [] 

    def activedriver(self):
        self.driver.get(self.url)
        print("first function done") 

    def getdata(self):
        self.activedriver()
        with open('data.txt') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    print(line.strip())
                    self.list1.append(line.strip())
                else:
                    print(line.strip())
                    self.list2.append(line.strip())
        print(self.list1)
    
    def login(self):
        self.getdata()
        for usernamedata, passworddata in zip(self.list1, self.list2):
            try:
                username = driver.find_element("xpath", '//input[@name ="username"]')
                password = driver.find_element("xpath", '//input[@name ="password"]')
                Searchbutton = driver.find_element("xpath", '//button[@type = "submit"]')
                username.send_keys(usernamedata)
                password.send_keys(passworddata)
                Searchbutton.click()
                menubutton = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Settings"]')
                menubutton.click()
                settingbutton = driver.find_element("xpath", "//div[text()='Settings']")
                settingbutton.click()
                try:
                    input_field = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[2]/div/div/input")
                    input_field.clear()
                    usernameupdate =  "g743"
                    str1 = usernamedata
                    str2 = "8787"
                    usernameupdate = str1 + str2
                    input_field.send_keys(usernameupdate)
                    submitbutton = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[10]/div/div/button")
                    submitbutton.click()
                    menubutton = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/a/div")
                    menubutton.click()
                    logout = driver.find_element("xpath", "//div[text()='Log out']")
                    logout.click()
                except:
                    menubutton = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/a/div")
                    menubutton.click()
                    logout = driver.find_element("xpath", "//div[text()='Log out']")
                    logout.click()

            except:
                driver.get("https://www.instagram.com/")
                    

if __name__ == "__main__":
   
    url = "https://www.instagram.com/"
    driver = webdriver.Chrome()
    scraper = euobserver(driver,url)
    driver.implicitly_wait(3)
    scraped = scraper.login()