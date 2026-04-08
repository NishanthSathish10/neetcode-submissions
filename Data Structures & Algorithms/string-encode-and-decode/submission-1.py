class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for word in strs:
            ans = ans + str(len(word))+ "#" + word

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            n = ""
            while s[j] != "#":
                n = n + s[j]
                j+=1
            n = int(n)
            ans.append(s[j+1:(j+n+1)])
            i = j+n+1

        return ans