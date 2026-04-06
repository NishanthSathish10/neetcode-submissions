class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict={}
        ans=[]
        for i in range(len(nums)):
            if (target - nums[i]) in seen_dict:
                ans.extend([seen_dict[target - nums[i]],i])
            seen_dict[nums[i]] = i

        return ans