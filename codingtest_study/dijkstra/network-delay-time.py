import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # 1. 인접 리스트(graph) 생성: 각 노드에서 출발 가능한 (도착 노드, 소요 시간)을 저장
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. 최소 힙 초기화: (현재까지의 누적 시간, 현재 노드)
        heap = [(0, k)]

        # 3. 거리 배열 초기화 (1번부터 n번 노드까지, 0번은 사용하지 않음)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0  # 시작 노드까지의 시간은 0

        # 4. 우선순위 큐를 활용한 다익스트라 알고리즘
        while heap:
            time, node = heapq.heappop(heap)  # 현재까지 누적 시간, 현재 노드

            # 이미 더 짧은 경로로 방문한 노드는 스킵
            if time > dist[node]:
                continue

            # 인접 노드들에 대해 거리 갱신 시도
            for neighbor, weight in graph[node]:
                new_time = time + weight  # 현재까지의 시간 + 엣지 가중치
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time  # 더 짧은 경로 발견 시 갱신
                    heapq.heappush(heap, (new_time, neighbor))  # 큐에 추가

        # 5. 모든 노드가 도달 가능한지 확인
        max_time = max(dist[1:])  # 0번 인덱스는 무시
        return max_time if max_time != float('inf') else -1  # 도달 불가능 시 -1