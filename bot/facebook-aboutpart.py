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
            cookie = {'name': 'c_user', 'value': '100094608188763'}
            self.driver.add_cookie(cookie)
            cookie = {'name': 'xs', 'value': '21%3Al4FtFpbxCVQTtQ%3A2%3A1688994118%3A-1%3A-1'}
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
        filename = 'super3.csv'
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
                
            
            
           
            #scroll function
            time.sleep(2)
            scroll_value = "window.scrollBy(0, window.innerHeight * 0.25);"
            driver.execute_script(scroll_value)
            
            
            # page_height = self.driver.execute_script("return document.body.scrollHeight")
            # quarter_height = page_height /4
            # while True:
            #     driver.implicitly_wait(6)
            #     self.driver.execute_script(f"window.scrollBy(0, {quarter_height});")
            #     time.sleep(1)
            #     driver.implicitly_wait(6)
            #     new_height = self.driver.execute_script("return document.body.scrollHeight")
            #     time.sleep(1)
            #     driver.implicitly_wait(6)
            #     if new_height == page_height:
            #         break
            #     page_height = new_height
            time.sleep(1)
            print("Scroll down complete")
            
            
        
            try:
                time.sleep(1)
                workandeducation = driver.find_element("xpath", '//span[text() ="Work and education"]')
                time.sleep(1)
                workandeducation.click()
                time.sleep(1)
            except:
                continue

            workandeducation = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(workandeducation))
            workunidata = []
            for work in workandeducation:
                print(work.text)
                workunidata.append(work.text)
            print(workunidata ,"here is all data related uni")
            new_string_WUS = ', '.join(workunidata)
            
            #######work data
            urldata.append(link) 
            
            NODATA = "NaN"
            try:
                work_value = []
                work1data = []
                work2data = []
                for item in workunidata:
                    if item.startswith('Worked at'):
                        work_value.append(item)
                print(len(work_value))
                if len(work_value) == 1:
                    work1data.append(work_value[0])
                    work2data.append(NODATA)
                elif len(work_value) >= 2:
                    work1data.append(work_value[0])
                    work2data.append(work_value[1]) 
                elif len(work_value) == 0:
                    workregax = workunidata.index('Work') + 1
                    touniregax = workunidata.index('University') 
                    worktouni = ', '.join(workunidata[workregax:touniregax])
                    print(worktouni)
                    if worktouni == 'No workplaces to show':
                        worktouni = "NaN"
                        print(worktouni)
                    work1data.append(worktouni)
                    work2data.append(NODATA)   
                else:
                    work1data.append(NODATA)
                    work2data.append(NODATA)
            except:
                work1data.append(NODATA)
                work2data.append(NODATA)

            print(work1data[0] ," worked placed 1")
            print(work2data[0] ," worked placed 2")
            workssdata.append(work1data[0])
            workssdata1.append(work2data[0])
            
            ###### uni and high school data 
            try:
                UNI1DATA = []
                UNI2DATA = []
                HIGHSCH1DATA = []
                HIGHSCH2DATA = []
                HIGH_values = []
                UNI_values = []
                for item in workunidata:
                    if item.startswith('Studied'):
                        UNI_values.append(item)
                    elif item.startswith('Went to'):
                        HIGH_values.append(item)
                if len(UNI_values) == 1:
                    UNI1DATA.append(UNI_values[0])
                    UNI2DATA.append(NODATA)
                elif len(UNI_values) >= 2:
                    UNI1DATA.append(UNI_values[0])
                    UNI2DATA.append(UNI_values[1])
                else:
                    UNI1DATA.append(NODATA)
                    UNI2DATA.append(NODATA)
                
                print(UNI1DATA[0] , "UNI1DATA")
                print(UNI2DATA[0] , "UNI2DATA")
                
                universityssdata.append(UNI1DATA[0])
                universityssdata1.append(UNI2DATA[0])
                
                
                if len(HIGH_values) == 1:
                    HIGHSCH1DATA.append(HIGH_values[0])
                    HIGHSCH2DATA.append(NODATA)
                elif len(HIGH_values) >= 2:
                    HIGHSCH1DATA.append(HIGH_values[0])
                    HIGHSCH2DATA.append(HIGH_values[1])
                else:
                    HIGHSCH1DATA.append(NODATA)
                    HIGHSCH2DATA.append(NODATA)
                    
                print(HIGHSCH1DATA[0] , "HIGHSCHOOLDATA1")
                print(HIGHSCH2DATA[0] ,"HIGHSCHOODATA2") 
                
                highdata.append(HIGHSCH1DATA[0])
                highdata1.append(HIGHSCH2DATA[0]) 
                                
            except:
                print("break during uni and high school")

            
            
            
            
            
           #here is placed  live data
           
            time.sleep(1)
            placelive = driver.find_element("xpath", '//span[text()="Places lived"]')
            time.sleep(1)
            placelive.click()
            time.sleep(1)
            livedplaced = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(livedplaced))
            placeddata = []
            for place in livedplaced:
                print(place.text)
                placeddata.append(place.text)
            print(placeddata ,"Placed data")
            new_string_placed = ', '.join(placeddata)
            print(new_string_placed ,"placed")
            placedsdata.append(new_string_placed)

            
            if len(placeddata) < 3:
                home_town_previous = "NaN"
                places_lived_next = "NaN"
                # print("Home Town:", home)
                # print("Current Town:", current_town)
           
            else:
                places_lived_next = None
                home_town_previous = None

                for index, item in enumerate(placeddata):
                    if item == 'Places lived' and index < len(placeddata) - 1:
                        places_lived_next = placeddata[index + 1]
                    elif item == 'Home town' and index > 0:
                        home_town_previous = placeddata[index - 1]
                        break  # Exit loop after the first occurrence of Home town

                # Replace None values with NaN
                places_lived_next = places_lived_next if places_lived_next is not None else math.nan
                
                
                home_town_previous = home_town_previous if home_town_previous is not None else math.nan

                print("Places lived next:", str(places_lived_next))
                print("Home town previous:", str(home_town_previous))
                if places_lived_next == "":
                    places_lived_next ="NaN"
                if home_town_previous == "":
                    places_lived_next ="NaN"
                if places_lived_next == " ":
                    places_lived_next ="NaN"
                if home_town_previous == " ":
                    places_lived_next ="NaN"
                    
                
            hometown.append(home_town_previous)
            currenttown.append(places_lived_next)           
                
                
            
           
           
           
           
        
            #contact
            
            time.sleep(1)
            contact = driver.find_element("xpath", '//span[contains(., "Contact and")]')
            time.sleep(1)
            contact.click()
            time.sleep(1)
            contactinfo = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(contactinfo))
            contactdata = []
            for con in contactinfo:
                print(con.text)
                contactdata.append(con.text)
            print(contactdata)
            time.sleep(1)
            new_string_contact = ', '.join(contactdata)
            print(new_string_contact ,"placed")
            contactsdata.append(new_string_contact)
            
            
            #data of contact info , website and basic info
            try:
                if len(contactdata) < 3:
                    contact_info_str = 'NaN'
                    websites_social_links_str = 'NaN'
                    basic_info_str = 'NaN'
                else:
                    contact_info_index = contactdata.index('Contact info') + 1
                    websites_social_links_index1 = contactdata.index('Websites and social links')
                    websites_social_links_index = contactdata.index('Websites and social links') + 1
                    basic_info_index = contactdata.index('Basic info')
                    gender_index = contactdata.index('Gender')

                    contact_info_str = ' '.join(contactdata[contact_info_index:websites_social_links_index1])
                    websites_social_links_str = ' '.join(contactdata[websites_social_links_index:basic_info_index])
                    basic_info_str = ' '.join(contactdata[basic_info_index+1:gender_index])

                    if contact_info_str.strip() == '' or contact_info_str == 'No contact info to show':
                        contact_info_str = 'NaN'
                    if websites_social_links_str.strip() == '' or websites_social_links_str == 'No links to show':
                        websites_social_links_str = 'NaN'
                    if basic_info_str.strip() == '':
                        basic_info_str = 'NaN'

                    print("Contact Info:", contact_info_str)
                    print("Websites and Social Links:", websites_social_links_str)
                    print("Basic Info:", basic_info_str)
            except:
                contact_info_str = 'NaN'
                websites_social_links_str = 'NaN'
                basic_info_str = 'NaN'
            contact_info.append(contact_info_str)
            website_social.append(websites_social_links_str)
            genderdata.append(basic_info_str)    

            
            #family
            
            time.sleep(1)
            family = driver.find_element("xpath", '//span[text()="Family and relationships"]')
            time.sleep(1)
            family.click()
            
            time.sleep(1)
            familyinfo = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(familyinfo))
            familydata = []
            for fam in familyinfo:
                print(fam.text)
                familydata.append(fam.text)
            print(familydata ,"here data family data")
            new_string_family = ', '.join(familydata)
            print(new_string_family ,"placed")
            familysdata.append(new_string_family)
            
            #family data 
            try:
                if len(familydata) < 2:
                    relationship_data = 'NaN'
                    family_members_data = 'NaN'
                else:
                    relationship_index = familydata.index('Relationship') + 1
                    family_members_index = familydata.index('Family members')
                    
                    
                    
                    

                    relationship_data = ', '.join(familydata[relationship_index:family_members_index])

                    if relationship_data.strip() == '' or relationship_data == 'No relationship info to show':
                        relationship_data = 'NaN'

                    family_members_data = ', '.join(familydata[family_members_index + 1:-1])

                    if family_members_data.strip() == '' or family_members_data == 'No family members to show':
                        family_members_data = 'NaN'

                    if relationship_data == 'No relationship info to show':
                        relationship_data = 'NaN'

                    if family_members_data == 'No family members to show':
                        family_members_data = 'NaN'

                    print("Relationship:", relationship_data)
                    print("Family Members:", family_members_data)
            except:
                relationship_data = 'NaN'
                family_members_data = 'NaN'
                
             ####### relationshio data    
                
           
            unique_words = [] 
            words = relationship_data.split() 
            for word in words:
                if word not in unique_words:  
                    unique_words.append(word)
            if len(unique_words[-1]) == 4:
                unique_words = unique_words[:-1]
            new_string = " ".join(unique_words) 
            print(new_string)
            
            
            #######  family member data
            
            words2 = family_members_data.split() 
            unique_words2 = [] 
            for word2 in words2:
                if word2 not in unique_words2:  
                    unique_words2.append(word2)
            new_string2 = " ".join(unique_words2) 
            print(new_string2  ,"familydata")
            
            relationdata.append(new_string)
            family_data.append(new_string2)
            
            
                
            
            
            
        
            #detial
            
            time.sleep(1)
            detial = driver.find_element("xpath", '//span[contains(., "Details About")]')
            time.sleep(1)
            detial.click()
           
            time.sleep(1)
            detialinfo = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(detialinfo))
            detialdata = []
            for det in detialinfo:
                print(det.text)
                detialdata.append(det.text)
            print(detialdata ,"here is detial data")
            new_string_det = ', '.join(detialdata)
            print(new_string_det ,"placed")
            detialsdata.append(new_string_det)
            
            
            
            try:
                if len(detialdata) < 3:
                    about_value = 'NaN'
                    name_pronunciation_value = 'NaN'
                    other_names_value = 'NaN'
                    favourite_quotes_value = 'NaN'
                # Find the value after 'About Mishka'
                else:
                    about_index = detialdata[1]

                    # Find the value after 'Name pronunciation'
                    name_pronunciation_index = detialdata.index('Name pronunciation')
                    name_pronunciation_value = detialdata[name_pronunciation_index + 1]

                    # Find the value after 'Other names'
                    other_names_index = detialdata.index('Other names')
                    other_names_value = detialdata[other_names_index + 1]

                    # Find the value after 'Favourite Quotes'
                    favourite_quotes_index = detialdata.index('Favourite Quotes')
                    favourite_quotes_value = detialdata[favourite_quotes_index + 1]

                    # Replace specific values with "NaN"
                    values_to_replace = ['No additional details to show','No name pronunciation to show', 'No other names to show', 'No favourite quotes to show']

                    if about_index in values_to_replace:
                        about_value = 'NaN'

                    if name_pronunciation_value in values_to_replace:
                        name_pronunciation_value = 'NaN'

                    if other_names_value in values_to_replace:
                        other_names_value = 'NaN'

                    if favourite_quotes_value in values_to_replace:
                        favourite_quotes_value = 'NaN'

                    print("'About Mishka':", about_value)
                    print("'Name pronunciation':", name_pronunciation_value)
                    print("'Other names':", other_names_value)
                    print("'Favourite Quotes':", favourite_quotes_value)
            except:
                about_value = 'NaN'
                name_pronunciation_value = 'NaN'
                other_names_value = 'NaN'
                favourite_quotes_value = 'NaN'
            aboutsdata.append(about_value)
            pronun.append(name_pronunciation_value)
            othername.append(other_names_value) 
            favour.append(favourite_quotes_value)
                
            #event 
            
            time.sleep(1)                
            event = driver.find_element("xpath", '//span[text()="Life events"]')
            time.sleep(1)
            event.click()
            time.sleep(1)
            
            eventinfo = driver.find_elements("xpath", "//div[@class='x1iyjqo2']//span")
            print(len(eventinfo))
            if "No life events to show" in eventinfo:
                eventinfo.append(NODATA)
            else:
                eventdatasingle = []
                try:
                    for seve in eventinfo:
                        print(seve.text)
                        eventdatasingle.append(seve.text)
                    print(eventdatasingle ,"here is event -main")
                    
                    if len(eventdatasingle) < 3:
                        eventmain.append(NODATA)
                    else:
                        event_value = eventdatasingle[1:]
                        print("'event':", event_value)
                        new_string_event = '- '.join(event_value)
                        print(new_string_event ,"life-event-data")
                        eventmain.append(new_string_event)
                except:
                    eventmain.append(NODATA)
                    
                      
                    
                    
            
            
            #about data ---------------- here we add data of like
            time.sleep(1) 
            try:
                about = driver.find_element("xpath", '//span[text()="More"]')
                time.sleep(2)
                about.click()
            except:
                time.sleep(5)
                continue
           
           
           ###############here we get data of like
            likedata = []
            try:
                time.sleep(1)                
                sportsclick = driver.find_element("xpath", '//span[text()="Likes"]')
                time.sleep(1)
                sportsclick.click()
                try:
                    nolikedata = driver.find_element("xpath", '//span[contains(., "No Likes")]')
                    time.sleep(1)
                    print(nolikedata.text , "sportdata")
                    likealldata.append(NaNdata)
                except:
                    scroll_value = "window.scrollBy(0, window.innerHeight * 0.99);"
                    driver.execute_script(scroll_value)
                    scroll_value = "window.scrollBy(0, window.innerHeight * 0.50);"
                    driver.execute_script(scroll_value)
                    
                    time.sleep(2)
                    likecarddata = driver.find_elements("xpath", '//div[@class="xu06os2 x1ok221b"]//span')
                    time.sleep(1)
                    for like in likecarddata:
                        print(like.text)
                        likedata.append(like.text)
                    likeall = ' '.join(likedata[2:])
                    print(likeall ,"here is like all function")
                    likealldata.append(likeall)
            except:
                likealldata.append(NaNdata)
                
            
            time.sleep(3)
            scroll_value = "window.scrollTo(0, 10);"
            driver.execute_script(scroll_value)
            time.sleep(3)
            scroll_value = "window.scrollBy(0, window.innerHeight * 0.15);"
            driver.execute_script(scroll_value)
                    
            #####all other without scroll
              #     #####here we get data of
            # try:
            #     time.sleep(1)                
            #     sportsclick = driver.find_element("xpath", '//span[text()="Sports"]')
            #     time.sleep(1)
            #     sportsclick.click()
            #     nosportdata = driver.find_element("xpath", '//span[contains(., "No sports")]')
            #     time.sleep(1)
            #     print(nosportdata.text , "sportdata")
            # except:
            #     print("sportdata empty")
                
                
        #     print("@@@@@@@@@@@@@@@@@@@sport@@@@@@@@@@@@@@@2")
            
          
        #event 
        print(len(workssdata))
        print(len(workssdata1))
        print(len(universityssdata))
        print(len(universityssdata1))
        print(len(highdata))
        print(len(highdata1))
        print(len(currenttown))
        print(len(hometown))
        print(len(contact_info))
        print(len(website_social))
        print(len(genderdata))
        print(len(relationdata))
        print(len(family_data))
        print(len(aboutsdata))
        print(len(pronun))
        print(len(othername))
        print(len(favour))
   
        technologies= {
            "work place 1":workssdata,
            "work place 2":workssdata1,
            "University 1":universityssdata,
            "University 2":universityssdata1,
            "High School 1":highdata,
            "High School 2":highdata1,
            "Current Town": currenttown,
            "Home Town":hometown,
            "Contact info" :contact_info,
            "Websites and social links": website_social,
            "Basic info":genderdata,
            "Relationship":relationdata,
            "Family members":family_data,
            "About":aboutsdata,
            "Name pronunciation":pronun,
            "Other Names":othername,
            "Favourite Quotes":favour,
            "Life events":eventmain,
            "URl":urldata,
            "Like": likealldata
           
            
            }
        
        df = pd.DataFrame(technologies)
        df.to_csv("main300to400.csv",index=False)
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