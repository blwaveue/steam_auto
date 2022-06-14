#github @blwaveue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # the local of the chromedriver
wd = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
wd.implicitly_wait(15)
