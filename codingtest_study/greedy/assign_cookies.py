class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # 자녀 욕심 정렬
        s.sort()  # 쿠키 크기 정렬

        answer = 0  # 만족한 자녀 수
        j = 0       # 쿠키 인덱스

        for i in range(len(g)):
            while j < len(s):
                if s[j] >= g[i]:  # 해당 자녀를 만족시키는 쿠키가 있다면
                    answer += 1
                    j += 1       # 이 쿠키는 사용됐으므로 다음 쿠키로
                    break
                j += 1  # 이 쿠키는 너무 작으므로 다음 쿠키로
        return answer