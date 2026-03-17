from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))

search_box.send_keys("MR BEAN MAGIC CLIP")

search_box.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from webdriver_manager.firefox import GeckoDriverManager

# service = Service("geckodriver.exe")
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# driver.get("https://www.youtube.com")

# wait = WebDriverWait(driver,10)

# search_box = wait.until(
#     EC.presence_of_element_located((By.NAME,"search_query"))
# )

# search_box.send_keys("MR BEAN MAGIC CLIP")
# search_box.send_keys(Keys.RETURN)

# first_video = wait.until(
#     EC.element_to_be_clickable((By.XPATH,'(//a[@id="video-title"])[1]'))
# )

# first_video.click()

# time.sleep(40)

# driver.quit()