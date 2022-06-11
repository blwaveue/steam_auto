from selenium import webdriver
from selenium.webdriver.chrome.options import Options

wd_lists = {}

chrome_options = Options()
chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # 指定自己的chromedriver路径

accounts = ['zhouyantii', 'blwaveue3', 'blwaveue4']  # 暂时不用, 'price'
addresses = ['127.0.0.1:9527', "127.0.0.1:9222", "127.0.0.1:9025"]  # 暂时不用, "127.0.0.1:8888"

for address, account, i in zip(addresses, accounts, range(1, 4, 1)):
    chrome_options.add_experimental_option("debuggerAddress", address)
    wd = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    print('正在链接', 'wd' + str(i), ' 地址:', address)
    wd_lists[account] = wd

for key, value in wd_lists.items():
    print(key, ':', value.title)

for wd_list in wd_lists.keys():
    wd_lists[wd_list].implicitly_wait(10)
