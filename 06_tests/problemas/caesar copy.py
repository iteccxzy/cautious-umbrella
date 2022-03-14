'''
You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.
'''


def cipher(message, n=1):

    message = message.lower()

    ab = 'abcdefghijklmnopqrstuvwxyz'
    dot = [' ', ',', '.']
    r = []

    for i in message:
        if i in dot:
            r.append(i)
        else:
            x = ab.index(i)+n
            if x < 26:
                r.append(ab[x])
            else:
                x = x-26
                r.append(ab[x])

    print(''.join(r))


if __name__ == '__main__':
    cipher('abcd xyz', 4)
