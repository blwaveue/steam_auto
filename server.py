import time
import xlwings as xw
import schedule

from price import refresh_price
from to_sell import to_sell


def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print(time.localtime(time.time()))


count = 1
app = xw.App(visible=True, add_book=False)
wb = app.books.add()


def work():
    global count
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # ################################blwaveue4
    place1 = 'A' + str(count)
    place2 = 'B' + str(count)
    place3 = 'J' + str(count)
    wb.sheets['sheet1'].range(place1).value = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(2)
    wb.sheets['sheet1'].range(place2).value = refresh_price('blwaveue4', 'CNY')
    time.sleep(5)
    wb.sheets['sheet1'].range(place3).value = to_sell('blwaveue4')
    time.sleep(5)
    count += 1
    place2 = 'B' + str(count)
    place3 = 'J' + str(count)
    # ###############################blwaveue4
    wb.sheets['sheet1'].range(place2).value = refresh_price('blwaveue3', 'HKD')
    time.sleep(5)
    wb.sheets['sheet1'].range(place3).value = to_sell('blwaveue3')
    time.sleep(5)
    count += 1
    place2 = 'B' + str(count)
    place3 = 'J' + str(count)
    # ###############################zhouyantii
    wb.sheets['sheet1'].range(place2).value = refresh_price('zhouyantii', 'CNY')
    time.sleep(5)
    wb.sheets['sheet1'].range(place3).value = to_sell('zhouyantii')
    time.sleep(5)
    ###########################
    count += 1


schedule.every(90).minutes.do(work)
print(time.localtime(time.time()))
work()
# schedule.every(89).minutes.do(refresh_price, 'zhouyantii', 'CNY')
# schedule.every(90).minutes.do(refresh_price, 'blwaveue3', 'HKD')
# schedule.every(91).minutes.do(refresh_price, 'blwaveue4', 'CNY')
# schedule.every(92).minutes.do(to_sell, 'zhouyantii')
# schedule.every(93).minutes.do(to_sell, 'blwaveue3')
# schedule.every(94).minutes.do(to_sell, 'blwaveue4')


while True:
    schedule.run_pending()
    time.sleep(1)
#
