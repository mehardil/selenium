
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class vestiaire:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.list1 = []  
        self.list2 = [] 

    def activedriver(self):
        self.driver.get(self.url)
        print("first function done") 
    
    def login(self):
        self.activedriver()
        ### sign in button
        driver.add_cookie({"name":"MUID" , "value":"172BCE79DEA8646021A1DC0CDFC36507","Domain":".bing.com"})
        data = driver.get_cookies
        print(data)
        driver.refresh()

        # signin = driver.find_element("xpath", "//button[@id='user-login']")
        # signin.click()



        # cookiesdata = driver.find_element("xpath", "//button[@id='popin_tc_privacy_button_2']")
        # print(cookiesdata.text)
        # print("why accept not work")
        # cookiesdata.click()
        # time.sleep(2)
        

       # login gmaildata and password 
        usermail = 'Support@collectorscage.com'
        password = '67667457'
        

        try: 
            #### enter mail and click on continue button
            gmaildata = driver.find_element("xpath", "//input[@id='welcomeEmail']")
            gmaildata.send_keys(usermail)
            continuebutton = driver.find_element("xpath", "//button[@type='submit']")
            continuebutton.click()

            #### enter password and click on login button
            passworddata = driver.find_element("xpath", "//input[@id='loginPassword']")
            passworddata.send_keys(password)
            loginbutton = driver.find_element("xpath", "//button[@type='submit']")
            loginbutton.click()
            time.sleep(2)

            ###case 2 -->if go to login page
        except:
            #login input -uservalue
            logingmaildata = driver.find_element("xpath", "//input[@id='user_email']")
            logingmaildata.send_keys(usermail)
            #login pass value
            loginpassworddata = driver.find_element("xpath", "//input[@id='user_password']")
            loginpassworddata.send_keys(password)
            #click on connect button
            connectbutton = driver.find_element("xpath", "//button[@data-cy='login_submit_connect_btn']")
            connectbutton.click()
            time.sleep(2)
            

         
        
        
        
if __name__ == "__main__":
   
    url = "https://www.vestiairecollective.com/"
    driver = webdriver.Chrome()
    scraper = vestiaire(driver,url)
    driver.implicitly_wait(5)
    scraped = scraper.login()
    