"""
Tolkein's publisher wishes to implement an online store for the "Lord of the Rings"
and "The Hobbit" books. Each book costs $10. However, if 2 titles are purchased,
a 5% discount will be received, i.e. purchasing "Fellowship of the Ring" and "Two Towers"
will cost $19. If 3 different titles are purchased, a 10% discount will be received. 
The purchase of all 4 different titles will receive a 20% discount.
An additional single title will be full-price.
"""

def calculate_cart_total(a):
    c,d = 0,{k:a.count(k) for k in set(a)}
    while d:
        c += 10*len(d)*(1-{1:0,2:.05,3:.1,4:.2}[len(d)])
        for k in d: d[k] -= 1
        d = {k:d[k] for k in d if d[k]}
    return c