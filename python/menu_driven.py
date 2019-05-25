#!/usr/bin/python

item1 = input('Enter the name of item 1: ')
price1 = input ("Enter the price of {}: ".format(item1))

item2 = input('Enter the name of item 2: ')
price2 = input ("Enter the price of {}: ".format(item2))

qty1 = input('Enter the number of {} ordered: '.format(item1))
qty2 = input('Enter the number of {} ordered: '.format(item2))

print "######### MENU #########"
print '1. {} ------> {}\n2. {} ------> {}'.format(item1, price1, item2, price2)
print "######### QUANTITY #########"
print '1. {} ------> {}\n2. {} ------> {}'.format(item1, qty1, item2, qty2)
print "######### BILL #########"
print "Total Bill = Rs. %f" % (qty1 * price1 + qty2 * price2)
