def solution(answers):
    
    result = []

    cnt = [0, 0, 0]
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, answer in enumerate(answers):

        if a[i%len(a)] == answers[i]:
            cnt[0] += 1
        if b[i%len(b)] == answers[i]:
            cnt[1] += 1
        if c[i%len(c)] == answers[i]:
            cnt[2] += 1
    
    for idx, x in enumerate(cnt):
        if x == max(cnt):
            result.append(idx+1)

    return result


# solution([1, 1])
    
