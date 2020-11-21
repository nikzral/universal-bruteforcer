# Universal Bruteforcer
A simple python 2 password bruteforce tool, compatible with nearly any login. Powered by Selenium.

# DISCLAIMER [PLEASE READ THIS]
This tool was created as a demonstration of my python skills, and MUST not be used for any malicious purposes. I claim no resposibility for anyt damage caused with this tool.

# Install
The dependencies for this tool are listed below:
  `Python 2`
  `Selenium`
  `Chromedriver`
  
## Selenium Webdriver Download
  `pip install selenium`
  
## Chromedriver Download
  You may download the version of chromedriver that corresponds to your version of chrome <a href="https://chromedriver.chromium.org/">here</a> 
  
# Setup
`driver = webdriver.Chrome("Path to the chromedriver excecutable")
url = "Enter the URL of the login here"
username = "Enter the username to be tried here"
wordlist = [Enter all logins to be tried here, in python list format]
usernamexpath = "Enter the html xpath of the username text box"
passwordxpath = "Enter the html xpath of the password text box"`

# Usage
`python /path/to/bruteforce.py`
