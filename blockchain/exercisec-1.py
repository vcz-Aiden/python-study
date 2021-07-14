import hashlib

"""
**********************************************
The 3 function below can be used to calculate the md5 and sha256 hash of a string.
Their use in demonstrate below in the main
************************************************
"""
def encode_message(message, enc):
    return message.encode(encoding=enc)


def hash_md5(message):
    # encode message using ascii encoding (try utf-8 for a different encoding)
    b_message = encode_message(message, 'ascii')
    hash_object = hashlib.md5(b_message)
    return hash_object.hexdigest()

def hash_sha256(message):
    # encode message using ascii encoding (try utf-8 for a different encoding)
    b_message = encode_message(message, 'ascii')
    hash_object = hashlib.sha256(b_message)
    return hash_object.hexdigest()
"""
***************************************************
"""


def calculate_nonce(s):
    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[0] == '0'):
            break

        nonce += 1

    print('a) (1 zero in front): Nonce = ', nonce)

    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[0] == '0' and hash_sha256(temp_s)[1] == '0'):
            break

        nonce += 1

    print('b) (2 zero in front): Nonce = ', nonce)

    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[0] == '0' and hash_sha256(temp_s)[1] == '0' and hash_sha256(temp_s)[2] == '0'):
            break

        nonce += 1

    print('c) (3 zero in front): Nonce = ', nonce)

    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[2] == 'c'):
            break

        nonce += 1

    print('d) ("c" at position 2): Nonce = ', nonce)

    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[2] == 'c' and hash_sha256(temp_s)[4] == 'c'):
            break

        nonce += 1

    print('e) ("c" at position 2,4): Nonce = ', nonce)

    nonce = 0
    while True:
        temp_s = s + str(nonce)
        if (hash_sha256(temp_s)[2] == 'c' and hash_sha256(temp_s)[4] == 'c' and hash_sha256(temp_s)[6] == 'c'):
            break

        nonce += 1

    print('f) ("c" at position 2,4,6): Nonce = ', nonce)

if __name__ == '__main__':

    test_string = "Hello, my name is Satoshi"
    print(hash_md5(test_string))
    print(hash_sha256(test_string))


    s = "UNI202 is amazing"
    calculate_nonce(s)

    """
    My results
    a) (1 zero in front): Nonce = 19
    b) (2 zeros in front): Nonce = 422
    c) (3 zeros in front): Nonce = 12019
    d) ("c" at position 2): Nonce = 6
    e) ("c" at position 2,4): Nonce = 100
    f) ("c" at position 2,4,6): Nonce = 4543
    """

