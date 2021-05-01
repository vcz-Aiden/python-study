import hashlib

s = input()

result = hashlib.sha256(s.encode())
print(result.hexdigest())