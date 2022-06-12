### 나의 코드...###

from collections import deque

def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    day = 0
    cnt = 0
    answer = []
    
    while p :
        cnt = 0
        res = []
        trash = []
        new_speed = []
        for i in range(1, len(p) + 1) :
            prog = p.popleft()
            speed = s.popleft()
            
            res.append(prog+speed)
            new_speed.append(speed)
            
            # print(res)
            # print(p)

            if prog+speed >= 100 :
                cnt += 1
                re = res.pop()
                new_speed.pop()
                trash.append(re)
                        
            if i == len(p) + len(res) + len(trash) :
                p = deque(res)
                s = deque(new_speed)
                day += 1
                if cnt != 0 :
                    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))




#### 답안 ####
# 1) count, time 변수를 설정해둔다. 

# 2) 첫번째가 100이 될때까지 loop 를 돌며 time 을 늘린다. 

#     else --> time+=1

# 3) (time =7) 이 되면  첫번째 값이(93) 100이 되어 if에 따라 pop 되고 count +=1

# 4) 현재 time 이 7이기 때문에 두번째 값(30)도 if에 따라 pop 되고 count +=1 

# 5) 세번째 값은 100이 안되기 때문에 loop를 돌며 time 을 늘리는데 

#     2) 번과 달리 그전에 완성된 친구들 count 값이 있기 때문에 이 친구들을 출시해줘야함 

#         따라서 answer 리스트에 append하고 count 초기화!!! 

#     그후에 loop를 돌며 time 을 늘리는데 

# 6) 세번째 값(55)이 100을 넘으면 count +=1 하고 

#     이 count 를 다시한번 answer 리스트에 append 해줌으로써 마지막 제품까지 출시 ! 

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer