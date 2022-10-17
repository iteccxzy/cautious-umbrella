'''
You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.
'''


def cipher(message, n=1):
    
    ab = {1: 'a',   2: 'b',     3: 'c',     4: 'd',     5: 'e',     6: 'f',     7: 'g',
          8: 'h',   9: 'i',     10: 'j',    11: 'k',    12: 'l',    13: 'm',    14: 'n',
          15: 'o',  16: 'p',    17: 'q',    18: 'r',    19: 's',
          20: 't',  21: 'u',    22: 'w',    23: 'y',    24: 'z'}

    # m = [c+n for i in message for c, v in ab.items() if i == v]
    m =[]
    for i in message:
        for c, v in ab.items():
            if i == v:
                m.append(c+n)

    # r = [ab[c] for i in m for c, v in ab.items() if i == c]
    r =[]
    for i in m:
        for c, v in ab.items():
            if i == c:
                r.append(ab[c])

    return ''.join(r)


if __name__ == '__main__':
    print(cipher('hola mundo'))
