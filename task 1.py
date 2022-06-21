python lab 1 complete selenium

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")

time.sleep(2)

driver.find_element_by_id("username").send_keys("F2019065220")
driver.find_element_by_id("password").send_keys("dEbHnU3@")
driver.find_element_by_id("loginbtn").click()
driver.find_element_by_css_selector("#page-wrapper > nav > div.d-inline-block.mr-3 > button > i").click()
driver.find_element_by_css_selector("#nav-drawer > nav > ul > li:nth-child(2)").click()

time.sleep(4)

driver.find_element_by_id("course-info-container-11507-17").click()
