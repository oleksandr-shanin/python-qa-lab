import string


def encode(text, shift=13):
    '''Takes string, returns that string encoded with Caesar cypher using
    'shift' as a key'''
    encoded_message_lst = []
    alphabet = string.printable
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encoding_dict = dict(zip(alphabet, shifted_alphabet))
    for char in text:
        # encoded_message_lst.append(encoding_dict[char])
        encoded_message_lst.append(encoding_dict.get(char, char))
    return ''.join(encoded_message_lst)


def decode(text, shift=13):
    return encode(text, -shift)
