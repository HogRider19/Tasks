"""
Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly.
Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!
What a bunch of cheapskates!
"""

def what_time_is_it(angle):
    hr, r = divmod(angle, 30)
    return f'{int(hr or 12):02}:{int(r*2):02}'