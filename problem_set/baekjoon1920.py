#use dictionary
#딕셔너리 기준이 조금 더 빨랐다.
n = int(input())
h_list = {}

for key in input().split(" ") :
    h_list[key] = 1

m = int(input())
for key in input().split(" ") :
    try :
        print(h_list[key])
    except KeyError :
        print(0)

#use set
n = int(input())
array = set(map(int, input().split(" ")))
m = int(input())
x = list(map(int, input().split(" ")))

for i in x :
    if i in array :
        print("1")
    else :
        print("0")