import kiteapp as kt
from time import sleep
with open('enctoken.txt', 'r') as rd:
	token = rd.read()
kite = kt.KiteApp("Rushabh", "OJF708", token)
kws = kite.kws() 



# Place Order
oid = kite.place_order(variety="amo", exchange='BSE',
		tradingsymbol='SBIN', transaction_type='BUY',
		quantity=5, product='CNC', order_type="LIMIT",
		price=820, validity="DAY")


print(oid)
'''
order = kite.orders()

print(order)

holding = kite.holdings()

print(holding)
'''