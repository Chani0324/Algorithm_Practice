# 문제
# 자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

# 출력
# N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

# 예제 입력 1 
# 53

# 예제 출력 1 
# 110101

### solution ###

num_to_bin = []

def solution(num):

    if num == 0:
        return
    elif num == 1:
        num_to_bin.insert(0, 1)
        return
    else :
        num_to_bin.insert(0, num % 2)
        solution(num // 2)


solution(53)
print("".join(map(str, num_to_bin)))



