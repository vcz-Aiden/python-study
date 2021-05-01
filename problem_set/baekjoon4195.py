n = int(input())

for i in range(n) :
    m = int(input())
    result_dic = {}

    for j in range(m) :
        names = input().split(" ")
        try :
            set1 = result_dic[names[0]]
        except KeyError :
            result_dic[names[0]] = set(names)
            set1 = result_dic[names[0]]

        try :
            set2 = result_dic[names[1]]
        except KeyError :
            result_dic[names[1]] = set(names)
            set2 = result_dic[names[1]]

        total = set1 | set2

        for name in list(total) :
            result_dic[name] = total

        print(len(total))