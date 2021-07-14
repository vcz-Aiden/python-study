# 해시: 완주하지 못한 선수

def solution(participant, completion):
    answer = {}

    for p in participant:
        try:
            answer[p] += 1
        except :
            answer[p] = 1

    for c in completion:
        if (answer[c] == 1):
            del answer[c]
        else :
            answer[c] -= 1

    return list(answer.keys())[0]

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))