class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        curr = 0
        for i in range(1, max(target) + 1):
            if i == target[curr]:
                ans.append('Push')
                curr += 1
            else:
                ans.append('Push')
                ans.append('Pop')

        return ans