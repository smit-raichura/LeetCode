def twoSum(nums: List[int], target: int) -> List[int]:
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    hash_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_dict:
            return [i,hash_dict[diff]]
        hash_dict[nums[i]] = i