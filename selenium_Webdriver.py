from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.yelp.com")

driver.find_element_by_xpath('.//*[@id="header-log-in"]/a').click()
sleep(5)
buttons = driver.find_elements_by_tag_name('button')
'''
for button in buttons:
    if button.text == 'post':
        button.click()
driver.close()
//*[@id="js_32"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div
'''