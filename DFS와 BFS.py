# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4

# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5

# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 

# 1000 999
# 1000 999
###################################################################

# def dfs(n, m, v, lst) :

#     answer = []

#     n_lst = list(range(1, n + 1))
#     num1 = n_lst.pop(v+1)

#     answer.add(num1)

#     while n_lst :
#         for idx, ls in enumerate(lst) :
#             if ls[idx][0] == answer[0]:
#                 answer.append(ls[idx][0])



#     return answer

# a = [[1, 2], [2, 3]]
# b = []

# b.append(a[0][0])
# print(b)

# print(list(range(1, 6)))


### 정답 ###
### https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1260%EB%B2%88-DFS%EC%99%80BFS ###
N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)