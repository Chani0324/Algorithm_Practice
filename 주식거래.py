## 주식거래
## stack과 queue를 이용하여 코드를 작성
## deque를 import 하여 리스트 양끝에서 data를 넣고 뺄수 있는 방식 사용.

## 코드 설명
# prices 리스트를 deque로 변환
# while문을 이용하여 q에 값이 존재(true)할 시
# deque(price)에서 맨 왼쪽에 있는 데이터를 뺌
# 반복문을 통해 반복할 때마다 sec에 +1을 해줌.
# deque(price)에 남아있는 값들과 뺀 값을 비교하여 뺀 값이 언제 더 커지는지 확인
# 뺀 값이 더 커지면 break를 통해 for 반복문 탈출하여 반복 횟수만큼 sec값을 answer에 append함. 
# q 값이 남아있을 경우 계속 반복 진행(q에 더이상 빼는게 없어질 때까지 진행(false))


from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []

    while q :
        sec = 0
        price = q.popleft()

        for i in q :
            sec += 1
            if price > i :
                break
        answer.append(sec)
    return answer