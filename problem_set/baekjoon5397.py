num = int(input())

for i in range(num) :
    stack1 = list()
    stack2 = list()
    for key in input() :
        if (key in '<>-') :
            if (key == "<"):
                if (stack1):
                    stack2.append(stack1.pop())
            elif (key == ">"):
                if (stack2):
                    stack1.append(stack2.pop())
            elif (key == "-"):
                if (stack1):
                    stack1.pop()
        else :
            stack1.append(key)

    stack2.reverse()
    print("".join(stack1 + stack2))