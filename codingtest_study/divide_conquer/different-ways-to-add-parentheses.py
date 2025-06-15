class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def recur(ex):
            answer = []

            for idx, ch in enumerate(ex): # 표현식 분해, index
                if (ch == "+") or (ch == "*") or (ch == "-"): # 연산자를 발견하면 (분할 기준)
                    # 왼쪽과 오른쪽 분할 연산자 기준으로
                    L = divide(ex[0:idx]) # 왼쪽 구간: 연산자 기준 왼쪽 부분식에 대해 재귀 호출
                    R = divide(ex[idx+1:]) # 오른쪽 구간: 연산자 기준 오른쪽 부분식에 대해 재귀 호출

                    # 분할된 결과 조합, 어차피 base case부터 진행하면 무조건 a + b 형식으로 나옴
                    for left in L:
                        for right in R:
                            if ch == '+':
                                answer.append(left + right) # 덧셈 결과 저장
                            if ch == '-':
                                answer.append(left - right) # 뺄셈 결과 저장
                            if ch == '*':
                                answer.append(left * right) # 곱셈 결과 저장

            # 숫자 하나만 있는 경우 걍 int 씌워서 배출
            if not answer:
                answer.append(int(ex))

            return answer

        return recur(expression)
