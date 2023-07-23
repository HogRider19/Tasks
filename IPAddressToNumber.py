"""
    While computers read and write IP addresses as a 32-bit number, we prefer to read them in dotted-decimal notation, which is basically
    the number split into 4 chunks of 8 bits, converted to decimal, and delmited by a dot.

    In this kata, you will create the function ipToNum that takes an ip address and converts it to a number,
    as well as the function numToIp that takes a number and converts it to an IP address string. Input will always be valid.
"""

def ip_to_num(ip):
    if isinstance(ip, str):
        x = []
        for i in ip.split('.'):
            binary = ((bin(int(i))))
            binary = binary[2:]
            if len(str(binary)) <8:
                binary = list(binary)
                binary.insert(0,str(0)*(8-len(binary)))
                x.append(''.join(binary))
            else:
                x.append(binary)
        x = ''.join(x)
        return (int(x, 2))
    
    
    
def num_to_ip(num):
    if isinstance(num, int):
        binary = bin(num)
        binary = binary[2:]
        if len(binary) < 32:
            binary = list(binary)
            binary.insert(0,str(0)*(32-len(binary)))
            binary = ''.join(binary)
        binary = [binary[i:i+8] for i in range(0, len(binary), 8)]
        returned = ''
        for i in binary:
            returned += f'{int(i, 2)}.'
        return returned[:-1]