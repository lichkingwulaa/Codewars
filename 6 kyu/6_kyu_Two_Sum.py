def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(sorted(two_sum([1,2,3], 4)), [0,2])
print(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
print(sorted(two_sum([2,2,3], 4)), [0,1])