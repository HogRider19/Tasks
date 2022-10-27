"""
Write a simple parser that will parse and run Deadfish.
Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
"""

def parse(data):

    value = 0
    result = []
    for command in data:
        
        if command == 'i':
            value += 1
        elif command == 'd':
            value -= 1
        elif command == 's':
            value **= 2
        elif command == 'o':
            result.append(value)

    return result



print(parse("ooo") == [0,0,0])
print(parse("ioioio") == [1,2,3])
print(parse("idoiido") == [0,1])
print(parse("isoisoiso") == [1,4,25])
print(parse("codewars") == [0])