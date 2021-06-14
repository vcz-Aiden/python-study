#lambda : 함수명 없이 1회용으로 사용할 함수를 정의하는 방법.

import functools

if __name__ == "__main__" :
    #sorting example
    strings = ['bob', 'charles', 'alexander3', 'teddy']
    strings.sort(key=lambda x:len(x))

    print(strings)


    #filter example
    nums = [1, 2, 3, 6, 8, 9]
    nums = list(filter(lambda x:x%2==0, nums))

    print(nums)



    #map example
    nums = [1, 2, 3, 6, 8, 9]
    nums = list(map(lambda x:x**2, nums))

    print(nums)



    #reduce example
    a = list(range(1, 11))
    print(functools.reduce(lambda x, y: x * y, a))

