#github @blwaveue
prise2 = {  # 176118270
    'will_sell_number_code': 'sell_176118270_qty',
    'owned_number_code': 'sell_176118270_qty_owned',
    'price_paid_code': 'sell_176118270_price_paid',
}
prise = {  # 176042493
    'will_sell_number_code': 'sell_176042493_qty',
    'owned_number_code': 'sell_176042493_qty_owned',
    'price_paid_code': 'sell_176042493_price_paid',
}
danger = {  # 176024744
    'will_sell_number_code': 'sell_176024744_qty',
    'owned_number_code': 'sell_176024744_qty_owned',
    'price_paid_code': 'sell_176024744_price_paid',
}
fracture = {  # 176185874
    'will_sell_number_code': 'sell_176185874_qty',
    'owned_number_code': 'sell_176185874_qty_owned',
    'price_paid_code': 'sell_176185874_price_paid',
}

owned_number_codes = []
will_sell_number_codes = []
price_paid_codes = []
cases = {
    'prise2': prise2,
    'prise': prise,
    'danger': danger,
    'fracture': fracture,
}
for case in cases.values():
    owned_number_codes.append(case.get('owned_number_code'))
for case in cases.values():
    will_sell_number_codes.append(case.get('will_sell_number_code'))
for case in cases.values():
    price_paid_codes.append(case.get('price_paid_code'))
