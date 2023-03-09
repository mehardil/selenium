# What is a proxy?
# A proxy is an intermediary between client requests and server responses
# An unauthenticated proxy server in Selenium can be set up with the following steps:
# step
# Import Selenium WebDriver from the package
# Define the proxy server (IP:PORT)
# Set ChromeOptions()
# Add the proxy server argument to the options
# Set up Chrome driver with proxy options


# from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy,ProxyType
# import time
# driver  = webdriver.Chrome('chrome')
# driver.get('https://whatismyipaddress.com')
# time.sleep(5)
# driver.quit()

# change proxy

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# change 'ip:port' with your proxy's ip and port
proxy_ip_port = '190.61.88.147:8080'
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
driver = webdriver.Chrome('your_absolute_path', desired_capabilities=capabilities)
driver.get('http://whatismyipaddress.com')
time.sleep(8)
driver.quit()


# change 'ip:port' with your proxy's ip and port