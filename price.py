#github @blwaveue
import re
import time

from selenium.webdriver.common.by import By

from downauto import downauto
from wd import wd

sell_prices_CNY = [0.46, 0.64, 0.62, 0.72]

########################################
factor = 2000
#######################################
urls = ['https://steamcommunity.com/market/listings/730/Prisma%202%20Case',
        'https://steamcommunity.com/market/listings/730/Prisma%20Case',
        'https://steamcommunity.com/market/listings/730/Danger%20Zone%20Case',
        'https://steamcommunity.com/market/listings/730/Fracture%20Case']
global d


def refresh_price():
    d = 0
    price = []
    nums = []
    global sell_prices_CNY
    for url, step in zip(urls, range(4)):
        wd.get(url)
        time.sleep(5)
        while len(wd.find_elements(By.CSS_SELECTOR,
                                                  '#market_commodity_forsale_table>.market_commodity_orders_table td')) == 0:
            print('将重试')
            time.sleep(15)
            wd.refresh()
            time.sleep(15)
            if len(wd.find_elements(By.CSS_SELECTOR,
                                                   '#market_commodity_forsale_table>.market_commodity_orders_table td')) != 0:
                break
        # have loaded the web######################################################################################
        print(wd.title)
        a = []
        for b in range(10):
            for c in range(180):
                if c == 179:
                    d = 1
                    break
                try:
                    a.append(wd.find_elements(By.CSS_SELECTOR,
                                                             '#market_commodity_forsale_table>.market_commodity_orders_table td')[
                                 b].text)
                    break

                except:
                    time.sleep(1)
        if d == 1:
            continue
        print(a[0], a[1])
        print(a[2], a[3])
        print(a[4], a[5])
        print(a[6], a[7])
        print(a[8], a[9])
        if int(a[9]) > 1 / float(re.findall(r"\d+\.?\d*", a[8])[0]) * factor:
            if int(a[7]) > 1 / float(re.findall(r"\d+\.?\d*", a[6])[0]) * factor:
                if int(a[5]) > 1 / float(re.findall(r"\d+\.?\d*", a[4])[0]) * factor:
                    if int(a[3]) > 1 / float(re.findall(r"\d+\.?\d*", a[2])[0]) * factor:
                        if int(a[1]) > 1 / float(re.findall(r"\d+\.?\d*", a[0])[0]) * factor:
                            price.append(float(re.findall(r"\d+\.?\d*", a[0])[0]))
                    else:
                        price.append(float(re.findall(r"\d+\.?\d*", a[2])[0]))
                else:
                    price.append(float(re.findall(r"\d+\.?\d*", a[4])[0]))
            else:
                price.append(float(re.findall(r"\d+\.?\d*", a[6])[0]))
        else:

            price.append(sell_prices_CNY[step])

        # remove the case if the price is unsuitable############################################################################################
        time.sleep(5)
        num = int(wd.find_element(By.ID, 'my_market_selllistings_number').text)
        nums.append(num)
        print(num)
        if num > 1000:
            downauto(50)
            time.sleep(5)
        elif num > 500:
            downauto(15)
            time.sleep(5)
        elif num > 200:
            downauto(6)
            time.sleep(5)
        elif num > 50:
            downauto(2)
            time.sleep(5)
        sell_prices_CNY = price
        price = sell_prices_CNY


    print('price updated：', price)

    return price + nums
