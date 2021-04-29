num = int(input())

for i in range(num) :
    list_length, idx = tuple(map(int, input().split(" ")))
    priority_list = list(map(int, input().split(" ")))

    print_count = 0

    while True :
        if (priority_list[0] == max(priority_list)) :
            del priority_list[0]
            print_count += 1

            if (idx == 0):
                print(print_count)
                break
            else:
                idx -= 1
        else :
            priority_list.append(priority_list[0])
            del priority_list[0]
            if (idx == 0):
                idx = len(priority_list) - 1
            else:
                idx -= 1