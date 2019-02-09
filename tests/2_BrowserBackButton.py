from selenium import webdriver
import time
browser='chrome'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/chromedriver.exe")
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/geckodriver.exe")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser")

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("header_tab_hotels").click()
driver.back()
driver.find_element_by_id("header_tab_holidays").click()
driver.find_element_by_id("hp-widget__sfrom").send_keys("Goa")
driver.find_element_by_id("searchBtn").click()
time.sleep(5)
driver.back()
driver.forward()