import time

from selenium import webdriver

driver = webdriver.chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")

time.sleep(2)

driver.find_element_by_id("username").send_keys("yourID")
driver.find_element_by_id("password").send_keys("yourPassword")
driver.find_element_by_id("loginbtn").click()

time.sleep(4)

driver.find_element_by_id("course-info-container-11507-17").click()
