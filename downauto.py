#github @blwaveue
import re
import time
from datetime import date
from datetime import datetime
from selenium.webdriver.common.by import By
from wd import wd


# eventlet.monkey_patch()

def days_between(d1):
    today = date.today()
    d2 = today.strftime("%m-%d")
    d1 = datetime.strptime(d1, "%m-%d")
    d2 = datetime.strptime(d2, "%m-%d")
    return abs((d2 - d1).days)


def downauto(clicks):
    a = 1
    for i in range(3600):
        try:
            date = \
            re.findall(r'\d+', wd.find_elements(By.CLASS_NAME, 'market_listing_right_cell')[5].text)[
                0] + '-' + \
            re.findall(r'\d+', wd.find_elements(By.CLASS_NAME, 'market_listing_right_cell')[5].text)[1]
            # dates = wd.find_elements(By.CLASS_NAME, 'market_listing_right_cell')#long code equade this short codes
            # date = re.findall(r'\d+', dates[5].text)
            # date = date[0] + '-' + date[1]
            if days_between(date) > 3:
                time.sleep(1)
                wd.find_element(By.CLASS_NAME, 'item_market_action_button_contents').click()
                time.sleep(2)
                wd.find_element(By.ID, "market_removelisting_dialog_accept").click()
                time.sleep(3)
                if len(wd.find_elements(By.CSS_SELECTOR,
                                                       '[style="opacity: 0.8; display: none;"]')) == 0:
                    wd.refresh()
                    print('refresh')
                    time.sleep(10)
                print('remove x', a)
                if a == clicks:
                    break
                a = a + 1
            else:
                break
        except:
            time.sleep(1)
