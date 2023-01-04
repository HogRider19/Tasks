"""
A string where each character represents
one second, with the following possible values.
'.' No event 'P' Button has been pressed
'O' Obstacle has been detected (supersedes P)
As an example, '..P....' means that nothing happens for two seconds,
then the button is pressed, then no further events.
A string where each character represents one second and indicates
the position of the door (0 if fully closed and 5 fully open).
The door starts moving immediately,
hence its position changes at the same second as the event
"""

def controller(events: list) -> str:
    possition = 0
    direction = 1
    is_stop = True
    result = ''

    for event in events:
        if event in 'P':
            is_stop = not is_stop
            
        elif event == 'O':
            direction *= -1
        
        if not is_stop:
            possition += direction

        if possition in [0,5]:
            is_stop, direction = True, 1 if possition == 0 else -1

        result += str(possition)
    return result


assert controller('..........') == '0000000000'
assert controller('P....') == '12345'
assert controller('P.P..') == '12222'
assert controller('..P...O...') == '0012343210'
    