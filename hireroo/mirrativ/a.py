# def solution(nums, target):
#     # TODO: Implement me!
#     lg = len(nums)
#     for i in range(lg):
#         for j in range(i+1, lg):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


import bisect
def solution(nums, target):
    # TODO: Implement me!
    lg = len(nums)
    nums.sort()
    # print(nums)
    for i in range(lg):
        target2 = target-nums[i]
        ind = bisect.bisect_left(nums, target2)
        if 0<=ind<lg and nums[ind]==target2:
            print(i, ind)
            return [i, ind]
        # break
        # left=i
        # right=lg
        # while abs(left-right)>1:
        #     mid = (left+right)//2

# nums = [1,3,7,4]
# # nums = [1,3,4,7,5]
# target = 7
# print(solution(nums, target))


from collections import defaultdict
def solution(nums, target):
    # TODO: Implement me!
    dic = defaultdict(str)
    lg = len(nums)
    for i in range(lg):
        dic[nums[i]] = i
    print(dic)
    for i in range(lg-1):
        target2 = target-nums[i]
        if dic[target2] != "" and dic[target2] != i:
            # print('aaa')
            return [i, dic[target2]]
        

# nums = [1,3,7,4]
# nums = [1,3,4,7,5]
nums = [3,2,4]
target = 6
print(solution(nums, target))