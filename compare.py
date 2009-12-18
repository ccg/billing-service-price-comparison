#!/usr/bin/env python

def spreedly(transactions):
    """
    http://spreedly.com/info/pricing/

    >>> spreedly(0)
    19.0
    >>> spreedly(100)
    39.0
    """
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
    """
    http://chargify.com/pricing-and-signup/

    >>> chargify(49)
    0.0

    Their pricing is scheme is ambiguous. It says 50 customers are free,
    but then it says 50 to 500 customers cost $49. So is customer number 50
    free, or does he cost $49?

    >>> chargify(51)
    49.0
    >>> chargify(499)
    49.0

    Same ambiguity exists at each jump point: 500, 5000, 10000, 15000.

    >>> chargify(500) >= 49.0 and chargify(500) <= 249.0
    True

    >>> chargify(501)
    249.0
    >>> chargify(4999)
    249.0
    >>> chargify(5001)
    749.0
    >>> chargify(9999)
    749.0
    >>> chargify(10001)
    1499.0
    >>> chargify(14999)
    1499.0
    >>> chargify(15001)
    2499.0
    >>> chargify(50000)
    2499.0
    """
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
    from optparse import OptionParser
    opts = OptionParser()
    opts.add_option('-t', '--test', action='store_true', help="Run tests")
    opts.add_option('-m', '--max', default=10000, help="Max customers")
    opts.add_option('-f', '--file', default='prices.txt', help="Output file")
    options, arguments = opts.parse_args()
    if options.test:
        import doctest
        doctest.testmod(verbose=True)
    max_customers = options.max
    f = open(options.file,'w')
    print >>f, "# num_customers\tchargify\tspreedly\tcheddargetter"
    for c in xrange(max_customers):
        print >>f, "%d\t%d\t%d\t%d" % (c, chargify(c), spreedly(c), cheddargetter(c))
    f.close()
