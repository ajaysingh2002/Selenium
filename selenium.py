from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(3)
username=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("ajay.pradhan3585")
Password=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("*******")
login=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mount_0_0_Bl']/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div/div/div/div/svg").click()
