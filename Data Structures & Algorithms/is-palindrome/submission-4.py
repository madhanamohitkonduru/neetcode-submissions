class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if (ord(i.lower()) in range(ord('a'), ord('z')+1)) or (ord(i.lower()) in range(ord('0'), ord('9')+1)):
                new_s += i.lower()
        # O(n)
        l = 0
        r = len(new_s) -1

        while l<r:
            if new_s[l] != new_s[r]:
                return False
            l+=1
            r-=1

        return True