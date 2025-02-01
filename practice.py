from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "/Users/doudouu0504/Desktop/chromedriver-mac-arm64/chromedriver"

if selenium.__version__.startswith("4"):
    driver = webdriver.Chrome(service=Service(PATH))
else:
    driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://www.youtube.com/")
search = driver.find_element(By.NAME, "search_query")
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

# 等待元素出現
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"]'))
)

# 取得標題
titles = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
for title in titles:
    print(title.text)

input("按 Enter 鍵結束程式並關閉瀏覽器...")
driver.quit()
