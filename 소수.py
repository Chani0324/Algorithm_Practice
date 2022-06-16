# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# "17"	3
# "011"	2
# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

# 11과 011은 같은 숫자로 취급합니다.

from itertools import permutations

def solution(numbers):
    answer = 0

    num_list = list(numbers)
    per_list = []
    # print(list(permutations(num_list, 2))[0][0])
    # print(list(permutations(num_list, 1)))

    # test01 = "".join(map(str, list(permutations(num_list, 2))[0]))
    # per_list.append(test01)
    # print(per_list)
        
    # map 한번 더 써서 int로 바꾸고, 반복문 써서 나눗셈(나누기는 sqrt써서 그 숫자까지만.(올림 해주면 될듯))
    # 중복 제거용으로 set 써도 될듯.

    for i in range(1, len(num_list) + 1):
        per_list += list(permutations(num_list, i))

    print(per_list)
    per_list_r = [int("".join(map(str, i))) for i in per_list]
        
    print(per_list_r)
    per_set = set(per_list_r)

    for i in per_set:
        if i == 1 or i == 0:
            per_set = per_set - set([i])
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                per_set = per_set- set([i])

    answer = len(per_set)
    return answer


print(solution("011"))