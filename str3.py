def cumulative_sum(nums):
    total = 0
    cumulativesum = []
    for num in nums:
       total += num
       cumulativesum.append(total)
    return cumulativesum

