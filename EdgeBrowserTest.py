import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# 驅動程式路徑
driver_path = 'path_to_edge_driver'

# 建立 Edge 瀏覽器選項
options = Options()
options.use_chromium = True

# 建立 Edge 瀏覽器服務
service = Service(driver_path)

# 建立 Edge 瀏覽器物件
driver = webdriver.Edge(service=service, options=options)

# 連續開啟網頁
websites = ['https://tw.yahoo.com', 'https://www.youtube.com/' , 'https://24h.pchome.com.tw/' , 'http://www.msn.com', 'https://www.bing.com']
for website in websites:
    driver.get(website)
    time.sleep(2)

print("Test result : Completely loads 5 top webpages")

# 關閉瀏覽器
driver.quit()
