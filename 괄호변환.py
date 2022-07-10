def solution(p):
    if len(p) == 0:
        return p
    else :
        p_lst = list(p)
        p_num_lst = [int(i.replace("(", "1").replace(")", "-1")) for i in p_lst]

        sum_num = 0

        for idx, val in enumerate(p_num_lst):
            sum_num += val 

            if sum_num == 0:
                u = p_num_lst[:idx+1]
                v = p_num_lst[idx+1:]

                break

        new_v = "".join([str(i).replace("-1", ")").replace("1", "(") for i in v])

        if u[0] != 1:
            u.pop(0)
            u.pop()
            
            new_u = "(" + "".join([str(i).replace("-1", "(").replace("1", ")") for i in u]) + ")"
            
            return new_u + solution(new_v)

        else :
            new_u = "".join([str(i).replace("-1", ")").replace("1", "(") for i in u])

            return new_u + solution(new_v)

        

print(solution("((()()))"))