import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

print("="*40, "Edge Brower Test", "="*40)
# driver path
driver_path = 'path_to_edge_driver'

# Create Edge browser option
options = Options()
options.use_chromium = True

# Create Edge service
service = Service(driver_path)

# Create Edge object
driver = webdriver.Edge(service=service, options=options)

# open 5 top webpages
websites = ['https://tw.yahoo.com', 'https://www.youtube.com/' , 'https://24h.pchome.com.tw/' , 'https://www.google.com.tw/', 'https://www.bing.com']
for website in websites:
    driver.get(website)
    time.sleep(2)

print("Edge Browser Test result : Completely loads 5 top webpages")

# close browser
driver.quit()
