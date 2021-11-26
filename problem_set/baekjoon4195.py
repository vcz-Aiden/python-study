n = int(input())

def find(x):
    if (x == network[x]['root']):
        return x
    else :
        root = find(network[x]['root'])
        network[x]['root'] = root
        return root

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if (root_x != root_y):
        network[root_y]['root'] = x
        network[root_x]['num'] += network[root_y]['num']

for i in range(n):
    network = dict()
    m = int(input())
    for j in range(m):
        f1, f2 = (input()).split(" ")

        if (f1 not in network.keys()):
            network[f1] = {
                'root': f1,
                'num': 1
            }

        if (f2 not in network.keys()):
            network[f2] = {
                'root': f2,
                'num': 1
            }

        union(f1, f2)
        print(network[find(f1)]['num'])