class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in nums:
        #     if nums.count(i) > 1:
        #         return True

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j and nums[i] == nums[j]:
        #             return True
                
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        
        # return len(nums) > len(set(nums))
        return False