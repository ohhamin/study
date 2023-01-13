import sys
import heapq

input = sys.stdin.readline

t = int(input())

for tc in range(t):

    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    # 그래프를 [선행해야 할 건물 수, [내가 지어져야 지을 수 있는 건물들]] 로 만듬
    graph = [[0, []] for i in range(n + 1)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][1].append(y)
        graph[y][0] += 1

    w = int(input())

    # 처음엔 ready 배열에 다 넣고 한번에 계산했음
    # 근데 이게 최선을 결과를 보장하지 않음

    # result = time[w]

    # while 1:
    #     endflag = 0
    #     ready = []
    #     for i in range(1, n + 1):
    #         if graph[i][0] == 0:
    #             if i == w:
    #                 endflag = 1
    #                 break
    #             ready.append(i)
    #             graph[i][0] -= 1
    #     if endflag == 1:
    #         break        
    #     tmptime = 0
    #     for i in ready:
    #         for j in graph[i][1]:
    #             graph[j][0] -= 1
    #         tmptime = max(tmptime, time[i])
    #     result += tmptime
    # print(result)

    # 그래서 힙큐를 사용하여 빨리 건설이 끝나는 애들 부터 처리

    result = 0
    ready = []
    for i in range(1, n + 1):
        if graph[i][0] == 0:
            ready.append([time[i], i])
    heapq.heapify(ready)

    while 1:
        now = heapq.heappop(ready)
        result += now[0]
        
        if now[1] == w:
            break
        # 레디 배열 안에 있는애들의 시간도 빼줌
        for i in ready:
            i[0] -= now[0]
        # 그리고 내가 지어져야 지어지는 건물들을 순회하며 선행건물 갯수를 1씩 빼고
        # 만약에 0이 되었다면 ready 힙에 추가해줌
        for i in graph[now[1]][1]:
            graph[i][0] -= 1
            if graph[i][0] == 0:
                heapq.heappush(ready, [time[i], i])
    print(result)