class Solution(object):
    def longestsubstrworepeatchars(self, str):
        if len(str) < 1:
            return 0

        longest = 0
        latestrepeating = -1
        positions = {}

        for i in range(0, len(str)):
            if str[i] in positions and latestrepeating < positions[str[i]]:
                latestrepeating = positions[str[i]]
        
        
            if i - latestrepeating > longest:
                longest = i - latestrepeating

            positions[str[i]] = i

        return longest
        


if __name__ == "__main__":
    print(Solution().longestsubstrworepeatchars("abcabcbb"))
    print(Solution().longestsubstrworepeatchars("bbbbb"))
    print(Solution().longestsubstrworepeatchars("pwwkew"))
