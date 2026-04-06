class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        for word in strs:
            flag = False
            count = Counter(word)
            for inner_list in ans:
                if Counter(inner_list[0]) == count:
                    inner_list.append(word)
                    flag = True
                    break 

            if not flag:
                ans.append([word])

        return ans
