n = int(input())
s = set()

k = input().split(" ")
for i in k:
    s.add(int(i))

n2 = int(input())
k = input().split(" ")
result = ""

for i in k:
    if (int(i) in s):
        result += "1 "
    else :
        result += "0 "

print(result[:-1])