import bisect

def solution(nums, target):
    # TODO: Implement me!
    lg = len(nums)
    ind = bisect.bisect_left(nums, target)
    return ind
        