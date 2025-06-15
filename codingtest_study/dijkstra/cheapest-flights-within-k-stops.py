import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        inf = float('inf')
        graph = [[] for _ in range(n)]
        distance = [[inf] * (k + 2) for _ in range(n)]  # [도시][경유 횟수]

        for fr, to, pr in flights:
            graph[fr].append((to, pr))

        H = []  # (도시, 가격, 경유 횟수)
        heapq.heappush(H, (src, 0, 0))
        distance[src][0] = 0

        while H:
            no, pr, st = heapq.heappop(H)

            if st > k:
                continue

            for next_no, total_pr in graph[no]:
                tmp_cost = pr + total_pr

                if tmp_cost < distance[next_no][st + 1]:
                    distance[next_no][st + 1] = tmp_cost
                    heapq.heappush(H, (next_no, tmp_cost, st + 1))

        # dst에 도달할 수 있는 경유 횟수들 중 최소 비용 반환
        answer = min(distance[dst])
        return -1 if answer == inf else answer