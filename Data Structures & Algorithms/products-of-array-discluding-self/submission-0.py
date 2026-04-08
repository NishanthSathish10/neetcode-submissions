class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero=set()
        prod = 1
        for idx,i in enumerate(nums):
            if i != 0:
                prod = prod * i
            else:
                zero.add(idx)

        ans = []

        for idx,i in enumerate(nums):

            if i == 0 and len(zero) > 1:
                ans.append(0)
            elif i == 0 and len(zero) == 1:
                ans.append(prod)
            elif len(zero) > 0:
                ans.append(0)
            else:
                ans.append(int(prod/i))

        return ans