def solution(nums, k):
    nums = nums[k-1::-1] + nums[:k-1:-1]
    return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))


"""
def solution(nums, k):
    numlst = nums[k-1::-1] + nums[:-k-1:-1]
    answer = []
    for i in range(len(numlst)-k+1):
        answer.append(sum(numlst[i:i+k]))

    return max(answer)
"""