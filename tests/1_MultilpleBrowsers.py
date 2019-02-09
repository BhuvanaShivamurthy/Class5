from selenium import webdriver

browser='chrome'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/chromedriver.exe")
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/geckodriver.exe")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/Bhuvana Shivamurthy/PycharmProjects/Class5/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser")

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("bhuvana.shivamurthy")
driver.find_element_by_id("pass").send_keys("bhuvana.shivamurthy")
try:
    driver.find_element_by_id("u_0_8").click()
    print("click is present")
except:
    print("elememt not presemt")















