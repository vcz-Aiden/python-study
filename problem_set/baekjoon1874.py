def start() :
    temp_list = []
    pp_list = []
    cur_num = 1

    n = int(input())

    for i in range(0, n):
        temp_num = int(input())
        while cur_num <= temp_num :
            temp_list.append(cur_num)
            cur_num += 1
            pp_list.append("+")
        if (temp_list[len(temp_list) - 1] == temp_num) :
            pp_list.append("-")
            temp_list.pop()
        else :
            print("NO")
            return

    print('\n'.join(pp_list))

start()