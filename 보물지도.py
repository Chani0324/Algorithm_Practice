def solution(n, a_lst, b_lst):

    answer = []

    for i in range(len(a_lst)):

        answer.append(bin(a_lst[i] | b_lst[i])[2:].zfill(n).replace("1", "#").replace("0", " "))

    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
