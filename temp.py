
# def UDS_CNY_rate():    #暂时用不到
#     # wd_lists['price'].switch_to.window(USD_CNY)#暂时不需要切换
#     print(wd_lists['price'].title)
#     wd_lists['price'].get('https://www.huilv.cc/USD_CNY/')
#     UDS_CNY_rate = wd_lists['price'].find_elements(By.CLASS_NAME, 'huilv_pink')
#     a = float(UDS_CNY_rate[1].text)
#     return a
#
# def UDS_HKD_rate():
#     # wd_lists['price'].switch_to.window(USD_HKD)#暂时不需要切换
#     print(wd_lists['price'].title)
#     wd_lists['price'].get('https://www.huilv.cc/USD_HKD/')
#     UDS_CNY_rate = wd_lists['price'].find_elements(By.CLASS_NAME, 'huilv_pink')
#     a = float(UDS_CNY_rate[1].text)
#     return a

# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)
# for handle in wd_lists['blwaveue4'].window_handles:
#     wd_lists['blwaveue4'].switch_to.window(handle)
#     if 'steam' in wd_lists['blwaveue4'].title:
#         break
# blwaveue4_sells = wd_lists['blwaveue4'].current_window_handle
# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)
# for handle in wd_lists['blwaveue4'].window_handles:
#     wd_lists['blwaveue4'].switch_to.window(handle)
#     if '新页标签' in wd_lists['blwaveue4'].title:
#         break
# blwaveue4_sell = wd_lists['blwaveue4'].current_window_handle
# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)
# for handle in wd_lists['price'].window_handles:
#     wd_lists['price'].switch_to.window(handle)
#     if '人民币' in wd_lists['price'].title:
#         break
# USD_CNY = wd_lists['price'].current_window_handle
# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)
# for handle in wd_lists['price'].window_handles:
#     wd_lists['price'].switch_to.window(handle)
#     if '港元' in wd_lists['price'].title:
#         break
# USD_HKD = wd_lists['price'].current_window_handle
# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)
# for handle in wd_lists['price'].window_handles:
#     wd_lists['price'].switch_to.window(handle)
#     if 'steam' in wd_lists['price'].title:
#         break
# steam = wd_lists['price'].current_window_handle
# # wd_lists['price'].switch_to.window(handle)  #切换窗口#暂时不需要切换
# time.sleep(1)


# print(UDS_CNY_rate())    #test
# print(UDS_HKD_rate())
# wd_lists['price'].switch_to.window(mainWindow)
# refresh_price_CNY('blwaveue4')
