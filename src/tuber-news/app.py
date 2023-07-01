from selenium import webdriver
from time import sleep
while True:
    driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')#provide the local download location of chrome driver for my case it is in downloads
    driver.get('https://www.tuber.org.in/')
    driver.maximize_window()
    sleep(3)
    driver.execute_script("window.scrollBy(0,2000)","")
    sleep(2)
    link = driver.find_element_by_link_text("SOURCE:Tubernews")
    link.click()
    sleep(3)
    driver.quit()
