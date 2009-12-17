#!/usr/bin/env python

def spreedly(transactions):
    return 19 + .20*transactions

def cheddargetter(customers):
    if customers > 50000:
        return 549+.02*(customers-50000)
    if customers > 10000:
        return 169.00 + 0.06 * (customers-10000)
    if customers > 1000:
        return 39 + .19*(customers-1000)
    if customers > 20:
        return 39.00
    return 0.

def chargify(customers):
    if customers > 15000:
        return 2499.
    if customers > 10000:
        return 1499.
    if customers > 5000:
        return 749.
    if customers > 500:
        return 249.
    if customers > 50:
        return 49.
    return 0.

if __name__ == '__main__':
    max_customers = 10000
    f = open('prices.txt','w')
    print >>f, "# num_customers\tchargify\tspreedly\tcheddargetter"
    for c in xrange(max_customers):
        print >>f, "%d\t%d\t%d\t%d" % (c, chargify(c), spreedly(c), cheddargetter(c))
    f.close()
