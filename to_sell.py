import time

from selenium.webdriver.common.by import By

from case import cases
from case import owned_number_codes
from case import price_paid_codes
from case import will_sell_number_codes
from wd import wd_lists


def to_sell(account):
    from price import sell_prices_CNY
    from price import sell_prices_HKD
    print(sell_prices_CNY)
    print(sell_prices_HKD)
    wd_lists[account].get(
        'https://steamcommunity.com/market/multisell?appid=730&contextid=2&items[]=Prisma%202%20Case&items['
        ']=Prisma%20Case&items[]=Danger%20Zone%20Case&items[]=Fracture%20Case')
    time.sleep(5)
    while len(wd_lists[account].find_elements(By.ID, will_sell_number_codes[0])) == 0:
        print('将重试')
        time.sleep(15)
        wd_lists[account].refresh()
        time.sleep(15)
        if len(wd_lists[account].find_elements(By.ID, will_sell_number_codes[0])) != 0:
            break
    #加载完毕####################
    print(wd_lists[account].title)
    # money = [
    #     float(re.findall(r"\d+\.?\d*", wd_lists[account].find_element(By.ID, 'marketWalletBalanceAmount').text)[0])]
    money = [wd_lists[account].find_element(By.ID, 'marketWalletBalanceAmount').text]
    nums = []
    for case, owned_number_code in zip(cases.keys(), owned_number_codes):  # 获取每种箱子数量
        a = int(wd_lists[account].find_element(By.ID, owned_number_code).text)
        nums.append(a)
        print(case, '一共有', a, '个')
    time.sleep(5)
    for will_sell_number_code, num in zip(will_sell_number_codes, nums):  # 填写数量
        a = wd_lists[account].find_element(By.ID, will_sell_number_code)
        a.clear()
        a.send_keys(num)
    time.sleep(5)
    if account == 'blwaveue3':
        for price, price_paid_code in zip(sell_prices_HKD, price_paid_codes):  ##填写价格
            a = wd_lists[account].find_element(By.ID, price_paid_code)
            a.clear()
            a.send_keys(price)
    else:
        for price, price_paid_code in zip(sell_prices_CNY, price_paid_codes):  ##
            a = wd_lists[account].find_element(By.ID, price_paid_code)
            a.clear()
            a.send_keys(price)

    time.sleep(5)
    sell_buttom = wd_lists[account].find_element(By.ID, 'market_multisell_createlistings')
    time.sleep(5)
    sell_buttom.click()
    print('已提交上架')
    return money
