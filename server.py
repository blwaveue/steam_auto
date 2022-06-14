#github @blwaveue
import time
import xlwings as xw
import schedule
from price import refresh_price
from to_sell import to_sell


def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


count = 1
app = xw.App(visible=True, add_book=False)
wb = app.books.add()


def work():
    global count
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    place1 = 'A' + str(count)
    place2 = 'B' + str(count)
    place3 = 'J' + str(count)
    wb.sheets['sheet1'].range(place1).value = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(2)
    wb.sheets['sheet1'].range(place2).value = refresh_price()
    time.sleep(5)
    wb.sheets['sheet1'].range(place3).value = to_sell()
    time.sleep(5)
    count += 1


schedule.every(90).minutes.do(work)
print(time.localtime(time.time()))
work()


while True:
    schedule.run_pending()
    time.sleep(1)
#
