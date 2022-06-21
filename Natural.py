import random
import urllib.request
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/nature")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
a = 0
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("YVj9w")
    if link1 == "YVj9w":
        Path = "natural_pic/Nature" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link, Path)
        if a == 10:
            break
        a = a + 1
    driver.close()



driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/animals")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
x = 0
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("YVj9w")
    if link1 == "YVj9w":
        Path = "natural_pic/Animal" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link, Path)
        if x == 10:
            break
        x = x + 1
    driver.close()



driver = webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/beach")
d = driver.find_element_by_css_selector("#app")
im = d.find_elements_by_tag_name("img")
z = 0
for i in im:
    link = i.get_attribute("src")
    link1 = i.get_attribute("YVj9w")
    if link1 == "YVj9w":

        Path = "natural_pic/Beach" + str(random()) + ".jpg"
        urllib.request.urlretrieve(link, Path)
        if z == 10:
            break
        z = z + 1
    driver.close()